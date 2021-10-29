from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from home.models import Data_set
import csv
#for ML
import pandas
from sklearn import linear_model
import joblib

# Create your views here.

def index(request):
    # return HttpResponse("this is home page")
    dataSet_allData = Data_set.objects.all().order_by('car_name')
    context = {
        "data" : dataSet_allData,
        "display" : "none"
    }
    if request.method == 'POST':

        car_name_title=request.POST["car_name"]
        km_driven=int(request.POST["km_driven"])
        dealer_type=int(request.POST["dealer_type"])
        owners_count=int(request.POST["owners_count"])
        present_price=0

        name_components = car_name_title.split(" (")
        car_name = name_components[0]
        year = int(name_components[1].split(")")[0])
        fuel_type = name_components[1].split(")")[1].split(" - ")[1]
        transmission_type = name_components[1].split(")")[1].split(" - ")[2]

        fuel=0
        transmission=0
        dealer_type_str=""

        if fuel_type=="Petrol" : 
            fuel=0
        elif fuel_type=="Diesel":
            fuel=1
        elif fuel_type=="CNG":
            fuel=2
        elif fuel_type=="LPG":
            fuel=3

        if transmission_type=="Manual" : 
            transmission=0
        elif transmission_type=="Automatic":
            transmission=1

        if dealer_type==0 : 
            dealer_type_str="Individual"
        elif dealer_type==1:
            dealer_type_str="Dealer/Broker"

        present_price = Data_set.objects.filter(car_name=car_name,year=year,fuel_type=fuel,transmission=transmission)
        for i in present_price:
            present_price=int((i.present_price)*100000)
            break


        model =  joblib.load("ml_model/used_car_price_predict_model.joblib")

        #year(user_input) , present_price(to be fetched from db) , km_driven , Fuel_Type ,Seller_Type , Transmission , Owner
        new_trial = model.predict([[year,present_price,km_driven,fuel,dealer_type,transmission,owners_count]])

        context={
            "car_name":car_name,
            "year" : year,
            "km_driven":km_driven,
            "dealer_type":dealer_type_str,
            "owners_count":owners_count,
            "present_price" :present_price ,
            "fuel_type" :fuel_type ,
            "transmission_type" :transmission_type ,
            "predicted_price":int(new_trial),
            "data" : dataSet_allData,
            "display" : "block"
                }
        return render(request,"index.html",context)
        
    return render(request,"index.html",context)

def list_cars(request):
    ans=Data_set.objects.all()

    context={
        "predicted_result":ans[2].car_name
    }        
    return render(request,"list.html",context)

