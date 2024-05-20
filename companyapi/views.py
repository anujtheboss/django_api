from django.http import HttpResponse,JsonResponse
def home_page(request):
    friends=[
        'ankit',
        'ravi',
        'hari'
    ]
    print("home page requested")
    return JsonResponse(friends,safe=False)



# to make api folder==>python manage.py startapp api