"""
URL configuration for companyapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home_page
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",home_page,name='homepage'),
    path("api/v1/",include('api.urls'))
 ]

# when we do initial request then the default app url is run
# now to go to api urls,api/v1 fro default app url is to be fire up

# get request is made to api through ....api/v1/..


# https//www.example.com
# https is a protocol for encrypted communication
# www.example.com is a domain name used to label the numerical ip address
# url=uniform resources locator is used to address the resources on the internet
# Domain names are mapped to IP addresses through the Domain Name System (DNS), which translates domain names into IP addresses and vice versa.



# http://127.0.0.1:8000/api/v1/companies/?format=api   
# 127.0.0.1 represents the IPv4 loopback address, which points to the local machine itself. It's often used for testing and development purposes.
# 8000 is the port number on which the server is listening for incoming HTTP requests. This port number is often used for local development servers.

# Path: /api/v1/companies/

# The path component specifies the endpoint or route within the API that the client wants to access. In this case, it's /api/v1/companies/, which likely corresponds to a resource or collection of resources related to companies.

# When a client sends a POST request to a server, it typically includes data in the request body, which the server can use to create a new resource or perform some other action.

#  "url": "http://127.0.0.1:8000/api/v1/companies/2/?format=json",
# url request to access the particular company data i.e.(company 2) inside the company in server file system