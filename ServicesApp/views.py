from django.shortcuts import render
from ServicesApp.models import Service
# Create your views here.


def services(request):

    service = Service.objects.all()

    return render(request, "services/services.html", {'service': service})

