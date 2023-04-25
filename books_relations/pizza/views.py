from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dough, Topping, Client, Pizza, Order
from .serializers import DoughSerializer, ToppingSerializer, ClientSerializer, PizzaSerializer, OrderSerializer

# Dough views


@api_view(['GET', 'POST'])
def dough_list_create(request):
    if request.method == 'GET':
        doughs = Dough.objects.all()
        serializer = DoughSerializer(doughs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DoughSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def dough_retrieve_update_destroy(request, pk):
    dough = get_object_or_404(Dough, pk=pk)

    if request.method == 'GET':
        serializer = DoughSerializer(dough)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DoughSerializer(dough, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dough.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Topping views


@api_view(['GET', 'POST'])
def topping_list_create(request):
    if request.method == 'GET':
        toppings = Topping.objects.all()
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def topping_retrieve_update_destroy(request, pk):
    topping = get_object_or_404(Topping, pk=pk)

    if request.method == 'GET':
        serializer = ToppingSerializer(topping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ToppingSerializer(topping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def client_list_create(request):

    if request.method == "GET":
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def client_retrieve_update_destroy(request, pk):
    client = get_object_or_404(Client, pk)

    if request.method == "GET":
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ClientSerializer(client, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
