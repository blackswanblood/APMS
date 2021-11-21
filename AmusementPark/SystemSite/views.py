from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.db import connection
from .forms import NameForm


def index (request):
    tourist_list = view_table('Tourist')
    staff_list = view_table('Staff')
    arcade_gift_list = view_table('ArcadeHasGift')
    cashier_worksat_list = view_table('Cashier_WorksAt')
    equipment_list = view_table('Equipment')
    gift1_list = view_table('Gift_1')
    gift2_list = view_table('Gift_2')
    machine_list = view_table( 'Machine')
    opop1_list = view_table('Operator_Operates_1')
    opop2_list = view_table('Operator_Operates_2')
    redeems_list = view_table('Redeems')
    rideMaintains_list = view_table('Ride_Maintains')
    technician_list = view_table('Technician')
    ticket1_list = view_table('Ticket_1')
    ticket2_list = view_table('Ticket_2')
    ticketforride_list = view_table('TicketForRide')
    tbt_list = view_table('TouristBuysTicket')
    tpm_list = view_table('TouristPlaysMachine')
    uses_list = view_table('Uses')



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

# def viewAllTourists(request):
#     tourist_list = Tourist.objects.raw('SELECT * FROM Tourist')
#     template = loader.get_template('SystemSite/viewalltourists.html')
#     context = {
#         'tourist_list': tourist_list,
#     }
#     return HttpResponse(template.render(context, request))

#
# def selectTable(model, table):
#     return model.objects.raw('SELECT * FROM ' + table)



# Insertion 
def insertion(request):
    tourist_list = view_table('Tourist')
    staff_list = view_table('Staff')
    template = loader.get_template('SystemSite/insertion.html')

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
                ID = form.cleaned_data['ID']
                Name = form.cleaned_data['Name']
                Age = form.cleaned_data['Age']
                Arcadept = form.cleaned_data['Arcadept']
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO Tourist VALUES (%s,%s,%s,%s)", [ID ,Name, Age, Arcadept])
                return HttpResponseRedirect('./')
    else:
        form = NameForm()
    
    context = {
        'tourist_list': tourist_list,
        'staff_list': staff_list,
        'form': form
    }
    return HttpResponse(template.render(context, request))


def view_table(name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM " + name)
        table = cursor.fetchall()
    return table



