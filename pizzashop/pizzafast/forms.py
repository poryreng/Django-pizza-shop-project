from django import forms
from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'pepperoni', 'chicken', 'ham', 'pineapple', 'peppers', 'mushrooms', 'onions']

# class ToppingForm(forms.ModelForm):
#     class Meta:
#         model = PizzaTopping
#         fields = ['id', 'pepperoni', 'chicken', 'ham']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['id', 'name', 'address', 'card_number', 'expiry_date', 'ccv']