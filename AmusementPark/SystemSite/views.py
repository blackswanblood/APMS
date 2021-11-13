from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Tourist

def index (request):
    return render(request, 'SystemSite/index.html')

def viewAllTourists(request):
    tourist_list = Tourist.objects.raw('SELECT * FROM Tourist')
    template = loader.get_template('SystemSite/viewalltourists.html')
    context = {
        'tourist_list': tourist_list,
    }
    return HttpResponse(template.render(context, request))


