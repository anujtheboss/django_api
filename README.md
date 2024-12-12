
## The purpose of this API is to allow external clients to interact with the Company model(database) and its associated data.
## because it provides a structured way for external applications or clients (like web browsers, mobile apps, or other servers) to interact with your Django application over the web using standard HTTP methods (GET, POST, PUT, DELETE).

## Serializers:
### CompanySerializer is a serializer class that converts Django model instances (Company) into JSON (or other content types) that can be sent over the web in the API responses.
### It also converts incoming JSON data into model instances when creating or updating records in the database (this process is called deserialization).
### The use of HyperlinkedModelSerializer provides an automatically generated hyperlink to the related resources (e.g., each company will have a URL pointing to its individual details).

## ViewSets:
### CompanyViewSet (which is not fully shown but implied by the code) would be a viewset class that defines the logic for handling HTTP requests related to companies.
###  viewset in Django REST Framework provides the logic for performing actions like listing, creating, updating, retrieving, and deleting objects.
### The viewset works with the CompanySerializer to handle these actions and automatically generate responses in the appropriate format (usually JSON).
### By registering this viewset with the router (router.register(r'companies', CompanyViewSet)), you create API endpoints that handle HTTP requests related to Company objects.

## Router:
DefaultRouter is a utility provided by DRF that automatically generates URL patterns for viewsets. You register the CompanyViewSet with the router, which means the router will create all the necessary URLs for interacting with companies.
By registering CompanyViewSet, the router generates the following endpoints:
GET /companies/: To list all companies.
POST /companies/: To create a new company.
GET /companies/{id}/: To get the details of a specific company.
PUT /companies/{id}/: To update a specific company.
DELETE /companies/{id}/: To delete a specific company
