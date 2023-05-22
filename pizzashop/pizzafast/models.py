from django.db import models
from datetime import date
# Create your models here.

class PizzaSize(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=12)

    def __str__(self):
        return self.size

class PizzaCrust(models.Model):
    id = models.AutoField(primary_key=True)
    crust = models.CharField(max_length=20)
    def __str__(self):
        return self.crust


class PizzaSauce(models.Model):
    id = models.AutoField(primary_key=True)
    sauce = models.CharField(max_length=20)

    def __str__(self):
        return self.sauce

class PizzaCheese(models.Model):
    id = models.AutoField(primary_key=True)
    cheese = models.CharField(max_length=20)

    def __str__(self):
        return self.cheese

# class PizzaTopping(models.Model):
#     id = models.AutoField(primary_key=True)
#     # topping = models.CharField(max_length=20, default=None, blank=True, null=True)

#     # def __str__(self):
#     #     return self.topping
#     pepperoni = models.BooleanField(default=False)
#     chicken = models.BooleanField(default=False)
#     ham = models.BooleanField(default=False)
#     pineapple = models.BooleanField(default=False)
#     peppers = models.BooleanField(default=False)
#     mushrooms = models.BooleanField(default=False)
#     onions = models.BooleanField(default=False)

    # # toppingChoices = (
    # #     ("PEPPERONI", "Pepperoni"),
    # #     ("CHICKEN", "Chicken"),
    # #     ("HAM", "Ham"),
    # #     ("PINEAPPLE", "Pineapple"),
    # #     ("PEPPERS", "Peppers"),
    # #     ("MUSHROOMS", "mushrooms"),
    # #     ("ONION", "Onion"),
    # #     ("NONE", "No Toppings"),
    # # )
    # id = models.AutoField(primary_key=True)
    # # toppings = models.CharField(max_length=12, choices=toppingChoices, default="NONE")
    # def __str__(self):
    #     return self.toppings

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
    sauce = models.ForeignKey(PizzaSauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(PizzaCheese, on_delete=models.CASCADE)
    # topping = models.ForeignKey(PizzaTopping, on_delete=models.CASCADE)
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    peppers = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    ccv = models.CharField(max_length=3)
    expiry_date = models.CharField(max_length=5)

