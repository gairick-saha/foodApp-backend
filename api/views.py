# from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
# from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from api.models import MenuCard, Menu
from .serializers import MenuCardSerializer, MenuSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE', ])
def simple_categories(request):

    if request.method == 'GET':
        category_list = MenuCard.objects.all()
        serializer = MenuCardSerializer(category_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuCardSerializer(data=request.data, )
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Menu Catagory Created"
            return JsonResponse(data=data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE', ])
def slug_categories(request, slug):

    print("slug categories : " + slug)

    if request.method == 'GET':
        qs = Menu.objects.filter(category__slug=slug)
        serializer = MenuSerializer(qs, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = MenuSerializer(data=request.data)
    #     data = {}
    #     if serializer.is_valid():
    #         serializer.save()
    #         data["success"] = "item Catagory Created"
    #         return JsonResponse(data=data, status=status.HTTP_200_OK)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE', ])
def simple_menu(request, slug):

    print("simple menu slug : " + slug)

    if request.method == 'GET':
        qs = Menu.objects.all()
        serializer = MenuSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "item Catagory Created"
            return JsonResponse(data=data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE',])
def slug_menu(request, slug, menu_slug):

    print("simple menu slug using shorted menu : " + slug)
    print("shorted menu slug : " + menu_slug)

    if request.method == 'GET':
        qs = Menu.objects.filter(category__slug=menu_slug)
        serializer = MenuSerializer(qs, many=True)
        return Response(serializer.data)
    