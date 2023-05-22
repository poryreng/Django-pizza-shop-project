from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PizzaSize)
admin.site.register(PizzaCrust)
admin.site.register(PizzaCheese)
admin.site.register(PizzaSauce)
# admin.site.register(PizzaTopping)
admin.site.register(Pizza)
admin.site.register(Delivery)