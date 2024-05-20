from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
        queryset=Company.objects.all()
        # It returns a queryset containing all the objects of the specified model. 
        # In this case, Company.objects.all() retrieves all instances of the Company model from the database.


        # This sets the queryset attribute of the CompanyViewSet class to fetch all Company objects from the database. 
        serializer_class=CompanySerializer
        # This sets the serializer_class attribute of the CompanyViewSet class to CompanySerializer, indicating which serializer class should be used to serialize/deserialize Company objects. 
        # This serializer will handle the conversion of Company model instances to and from JSON format when interacting with the API.
        # views is responsible for processing the user request and then providing response
        # view receive http request from user

# every model automatically gets an objects manager.The objects manager provides methods such as all(), filter(), get(), etc., for retrieving data from the database.