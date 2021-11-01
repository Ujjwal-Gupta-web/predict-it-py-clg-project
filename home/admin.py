from django.contrib import admin
from home.models import Listed_Cars
from home.models import Data_set

# Register your models here.
admin.site.register(Data_set)
admin.site.register(Listed_Cars)
