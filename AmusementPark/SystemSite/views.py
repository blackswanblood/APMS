from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Tourist, Staff

def index (request):
    tourist_list = Tourist.objects.raw('SELECT * FROM Tourist')
    staff_list = Staff.objects.raw ('SELECT * FROM Staff')

    tourist_count = len(list(tourist_list))
    staff_count = len(list(staff_list))

    template = loader.get_template('SystemSite/index.html')
    context = {
        'tourist_list': tourist_list,
        'tourist_count': tourist_count,
        'staff_count' : staff_count
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'SystemSite/index.html')

def viewAllTourists(request):
    tourist_list = Tourist.objects.raw('SELECT * FROM Tourist')
    template = loader.get_template('SystemSite/viewalltourists.html')
    context = {
        'tourist_list': tourist_list,
    }
    return HttpResponse(template.render(context, request))


