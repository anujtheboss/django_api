from rest_framework import serializers
from api.models import Company
# create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # HyperLinkedModelSerializer gives meta class
    class Meta:
        model=Company
        fields="__all__"  #means i want to include all fields of company model


# creating the virtual environment is good practice because
#  while installing some packages or models dependency problem may arise
#  some already installed components may avoid some dependency of currently running project to be installed



# python manage.py causes all the changes to reflect in database