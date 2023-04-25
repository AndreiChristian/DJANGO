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
    dough = serializers.PrimaryKeyRelatedField(queryset=Dough.objects.all())
    toppings = serializers.PrimaryKeyRelatedField(queryset=Topping.objects.all(), many=True)

    class Meta:
        model = Pizza
        fields = ['id', 'dough', 'toppings']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['dough'] = DoughSerializer(instance.dough).data
        representation['toppings'] = ToppingSerializer(instance.toppings.all(), many=True).data
        return representation

class OrderSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    pizza = serializers.PrimaryKeyRelatedField(queryset=Pizza.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'client', 'pizza', 'date']

