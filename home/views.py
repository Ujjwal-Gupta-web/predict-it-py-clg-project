from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from home.models import Data_set, Listed_Cars
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import csv

# for ML
import pandas
from sklearn import linear_model
import joblib

# Create your views here.


def index(request):
    # return HttpResponse("this is home page")
    dataSet_allData = Data_set.objects.all().order_by('car_name')
    context = {
        "data": dataSet_allData,
        "display": "none",
        "dis": "none"
    }
    if request.method == 'POST':

        car_name_title = request.POST["car_name"]
        km_driven = int(request.POST["km_driven"])
        dealer_type = int(request.POST["dealer_type"])
        owners_count = int(request.POST["owners_count"])
        present_price = 0

        name_components = car_name_title.split(" (")
        car_name = name_components[0]
        year = int(name_components[1].split(")")[0])
        fuel_type = name_components[1].split(")")[1].split(" - ")[1]
        transmission_type = name_components[1].split(")")[1].split(" - ")[2]

        fuel = 0
        transmission = 0
        dealer_type_str = ""

        if fuel_type == "Petrol":
            fuel = 0
        elif fuel_type == "Diesel":
            fuel = 1
        elif fuel_type == "CNG":
            fuel = 2
        elif fuel_type == "LPG":
            fuel = 3

        if transmission_type == "Manual":
            transmission = 0
        elif transmission_type == "Automatic":
            transmission = 1

        if dealer_type == 0:
            dealer_type_str = "Individual"
        elif dealer_type == 1:
            dealer_type_str = "Dealer/Broker"

        present_price = Data_set.objects.filter(
            car_name=car_name, year=year, fuel_type=fuel, transmission=transmission)
        for i in present_price:
            present_price = int((i.present_price)*100000)
            break

        model = joblib.load("ml_model/used_car_price_predict_model.joblib")

        # year(user_input) , present_price(to be fetched from db) , km_driven , Fuel_Type ,Seller_Type , Transmission , Owner
        new_trial = model.predict(
            [[year, present_price, km_driven, fuel, dealer_type, transmission, owners_count-1]])

        context = {
            "car_name": car_name,
            "year": year,
            "km_driven": km_driven,
            "dealer_type": dealer_type_str,
            "owners_count": owners_count,
            "present_price": present_price,
            "fuel_type": fuel_type,
            "transmission_type": transmission_type,
            "predicted_price": int(new_trial),
            "data": dataSet_allData,
            "display": "block",
            "dis": "none"
        }
        return render(request, "index.html", context)

    return render(request, "index.html", context)


def list_cars(request):
    if request.method == "POST":
        email = request.user.username
        list_car_name = request.POST["list-car_name"]
        list_price = request.POST["list-price"]
        list_km_driven = request.POST["list-km_driven"]
        list_owners_count = request.POST["list-owners_count"]
        list_year = request.POST["list-year"]
        list_fuel_type = request.POST["list-fuel_type"]
        list_transmission_type = request.POST["list-transmission_type"]
        list_phone_number = request.POST["list-phone_number"]
        list_seller_name = request.POST["list-seller_name"]
        list_city = request.POST["list-city"]
        list_number_plate = request.POST["list-number_plate"]

        car_dets = Listed_Cars(email=email, list_car_name=list_car_name, list_price=list_price, list_km_driven=list_km_driven, list_owners_count=list_owners_count, list_year=list_year, list_fuel_type=list_fuel_type,
                               list_transmission_type=list_transmission_type, list_phone_number=list_phone_number, list_seller_name=list_seller_name, list_city=list_city, list_number_plate=list_number_plate)

        car_dets.save()

        return render(request, "list.html", {"display": "", "message": "listed successfully"})

    return render(request, "list.html", {"display": "none", "message": ""})


def browse(request):
    all_cars = Listed_Cars.objects.all().order_by('list_price')
    context = {
        "all_listed_cars": all_cars
    }
    return render(request, "browse.html", context)


def handleSignup(request):
    if request.method == "POST":
        signup_email = request.POST['signup-email']
        signup_username = request.POST['signup-username']
        signup_password = request.POST['signup-password']

        myuser = User.objects.create_user(
            signup_email, signup_email, signup_password)
        myuser.first_name = signup_username
        myuser.save()

        return render(request, "index.html", {"dis": "", "dis_messsage": "Signup Success", "display": "none"})

    else:
        return render(request, "others.html", {"type": "warning", "message": "Bad request"})


def handleLogin(request):
    if request.method == "POST":
        login_email = request.POST["login-email"]
        login_password = request.POST["login-password"]

        user = authenticate(username=login_email, password=login_password)

        if user is not None:
            login(request, user)
            return render(request, "index.html", {"dis": "", "dis_messsage": "User Logged in", "display": "none"})
        else:
            return render(request, "others.html", {"type": "danger", "message": "Invalid credentials..try again"})

    else:
        return render(request, "others.html", {"type": "warning", "message": "Bad request"})


def handleLogout(request):
    logout(request)
    return render(request, "logout.html")


def dashboard(request):
    all_cars = Listed_Cars.objects.filter(
        email=request.user.username).order_by('list_price')
    if request.method == "POST":
        context = {
            "all_listed_cars": all_cars,
            "message": "Deleted",
            "display": ""
        }
        number_plate = request.POST['number_plate']
        car_det = Listed_Cars.objects.filter(list_number_plate=number_plate)
        car_det.delete()
        return render(request, "dashboard.html", context)

    context = {
        "all_listed_cars": all_cars,
        "display": "none"
    }

    return render(request, "dashboard.html", context)
