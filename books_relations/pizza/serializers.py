from rest_framework import serializers
from .models import Dough, Topping, Client, Pizza, Order


class DoughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dough
        fields = ['id', 'name']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id', 'name']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']


class PizzaSerializer(serializers.ModelSerializer):
    dough = DoughSerializer()
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ['id', 'dough', 'toppings']


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    pizzas = PizzaSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'pizzas', 'created_at', 'updated_at']
