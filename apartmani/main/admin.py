from django.contrib import admin
from .models import *

my_list = [Gost, Apartman, Rezervacija]
admin.site.register(my_list)
