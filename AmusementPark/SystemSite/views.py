from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def index (request):
    tourist_list = selectTable(Tourist, 'Tourist')
    staff_list = selectTable(Staff, 'Staff')
    arcade_gift_list = selectTable(Arcadehasgift, 'ArcadeHasGift')
    cashier_worksat_list = selectTable(CashierWorksat, 'Cashier_WorksAt')
    equipment_list = selectTable(Equipment, 'Equipment')
    gift1_list = selectTable(Gift1, 'Gift_1')
    gift2_list = selectTable(Gift2, 'Gift_2')
    machine_list = selectTable(Machine, 'Machine')
    opop1_list = selectTable(OperatorOperates1, 'Operator_Operates_1')
    opop2_list = selectTable(OperatorOperates2, 'Operator_Operates_2')
    redeems_list = selectTable(Redeems, 'Redeems')
    rideMaintains_list = selectTable(RideMaintains, 'Ride_Maintains')
    technician_list = selectTable(Technician, 'Technician')
    ticket1_list = selectTable(Ticket1, 'Ticket_1')
    ticket2_list = selectTable(Ticket2, 'Ticket_2')
    ticketforride_list = selectTable(Ticketforride, 'TicketForRide')
    tbt_list = selectTable(Touristbuysticket, 'TouristBuysTicket')
    tpm_list = selectTable(Touristplaysmachine, 'TouristPlaysMachine')
    uses_list = selectTable(Uses, 'Uses')



    tourist_count = len(list(tourist_list))
    staff_count = len(list(staff_list))
    redeem_count = len(list(redeems_list))
    ride_count = len(list(rideMaintains_list))

    template = loader.get_template('SystemSite/index.html')
    context = {
        'tourist_list': tourist_list,
        'staff_list' : staff_list,
        'arcade_gift_list': arcade_gift_list,
        'cashier_worksat_list' : cashier_worksat_list,
        'equipment_list' : equipment_list,
        'gift1_list': gift1_list,
        'gift2_list': gift2_list,
        'machine_list': machine_list,
        'opop1_list': opop1_list,
        'opop2_list': opop2_list,
        'redeems_list' : redeems_list,
        'rideMaintains_list' : rideMaintains_list,
        'technician_list' : technician_list,
        'ticket1_list' : ticket1_list,
        'ticket2_list' : ticket2_list,
        'ticketforride_list': ticketforride_list,
        'tbt_list': tbt_list,
        'tpm_list' : tpm_list,
        'uses_list' : uses_list,

        'tourist_count': tourist_count,
        'staff_count' : staff_count,
        'redeem_count' : redeem_count,
        'ride_count' : ride_count
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

def selectTable(model, table):
    return model.objects.raw('SELECT * FROM ' + table)


