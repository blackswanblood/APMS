from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def index (request):
    tourist_list = Tourist.objects.raw('SELECT * FROM Tourist')
    staff_list = Staff.objects.raw ('SELECT * FROM Staff')
    arcade_gift_list = Arcadehasgift.objects.raw('SELECT * FROM Arcadehasgift')
    cashier_worksat_list = CashierWorksat.objects.raw('SELECT * FROM Cashier_Worksat')


    tourist_count = len(list(tourist_list))
    staff_count = len(list(staff_list))

    template = loader.get_template('SystemSite/index.html')
    context = {
        'tourist_list': tourist_list,
        'staff_list' : staff_list,
        'arcade_gift_list': arcade_gift_list,
        'cashier_worksat_list' : cashier_worksat_list,
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

# def tableList(table, cmd):
#     table_list = table.objects.raw ('SELECT * FROM ' + str(table))
#     template = loader.get_template('SystemSite/index.html')
#     context = {
#         cmd : table_list
#     }
#     return 0


