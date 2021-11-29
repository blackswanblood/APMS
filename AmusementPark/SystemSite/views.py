from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.db import connection
from .forms import *


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
    arcade_list = view_table('Arcade')



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
        'arcade_list': arcade_list,

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
        form = insertTouristForm(request.POST)
        form1 = insertStaffForm(request.POST)
        if form.is_valid():
                ID = form.cleaned_data['ID']
                Name = form.cleaned_data['Name']
                Age = form.cleaned_data['Age']
                Arcadept = form.cleaned_data['Arcadept']
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO Tourist VALUES (%s,%s,%s,%s)", [ID ,Name, Age, Arcadept])
                return HttpResponseRedirect('./')
        if form1.is_valid():
                WorkID = form1.cleaned_data['WorkID']
                Name = form1.cleaned_data['Name']
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO Staff VALUES (%s,%s)", [WorkID ,Name])
                return HttpResponseRedirect('./')
    else:
        form = insertTouristForm()
        form1 = insertStaffForm()
    
    context = {
        'tourist_list': tourist_list,
        'staff_list': staff_list,
        'form': form,
        'form1': form1
    }
    return HttpResponse(template.render(context, request))

# Deletion
def deletion(request):
    arcade_list = view_table('Arcade')
    machine_list = view_table('Machine')
    template = loader.get_template('SystemSite/deletion.html')

    if request.method == 'POST':
        formA = deleteArcadeForm(request.POST)
        formM = deleteMachineForm(request.POST)
        if formA.is_valid():
                aName = formA.cleaned_data['ArcadeName']
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM Arcade WHERE Name = %s", [aName])
                return HttpResponseRedirect('./')
        if formM.is_valid():
                mName = formM.cleaned_data['MachineName']
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM Machine WHERE MName = %s", [mName])
                return HttpResponseRedirect('./')
    else:
        formA = deleteArcadeForm()
        formM = deleteMachineForm()
    
    context = {
        'arcade_list': arcade_list,
        'machine_list': machine_list,
        'formA': formA,
        'formM': formM
    }
    return HttpResponse(template.render(context, request))

# Update
def update(request):
    cashier_worksat_list = view_table('Cashier_WorksAt')
    arcade_list = view_table('Arcade')
    rideMaintains_list = view_table('Ride_Maintains')
    template = loader.get_template('SystemSite/update.html')

    if request.method == 'POST' and "Cashier ID" in request.POST:
        cashierID = request.POST['Cashier ID']
        arcade = request.POST['Arcade Name']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Cashier_WorksAt \
                            SET AName = %s  \
                            WHERE WorkID = %s", [arcade, cashierID])
        return HttpResponseRedirect('./')

    elif request.method == 'POST' and "RideName" in request.POST:
        form = MaintainanceForm(request.POST)
        if form.is_valid():
                RideName = form.cleaned_data['RideName']
                WorkID = form.cleaned_data['WorkID']
                EquipmentID = form.cleaned_data['EquipmentID']
                TimeofInspection = form.cleaned_data['TOI']

                with connection.cursor() as cursor:
                    cursor.execute("SELECT WorkID, EID FROM Ride_Maintains \
                                    WHERE RName = %s", [RideName])
                    (oldWorkID, oldEquipmentID) = cursor.fetchall()[0]

                    cursor.execute("UPDATE Ride_Maintains \
                        SET WorkID = %s, EID = %s, TimeofInspection = date(%s)  \
                        WHERE RName = %s", [WorkID, EquipmentID, TimeofInspection, RideName])

                    cursor.execute("UPDATE Uses \
                        SET WID = %s, EID = %s  \
                        WHERE WID = %s AND EID = %s ", [WorkID, EquipmentID, oldWorkID, oldEquipmentID])
                return HttpResponseRedirect('./')

    else: 
        form = MaintainanceForm()
    
    context = {
        'cashier_worksat_list': cashier_worksat_list,
        'arcade_list': arcade_list,
        'rideMaintains_list': rideMaintains_list,
        'form' : form
    }
    return HttpResponse(template.render(context, request))

# Selection 
def selection(request):
    tourist_list = view_table('Tourist')
    operator_list = view_table_natural_join(['Operator_Operates_1', 'Operator_Operates_2'])
    template = loader.get_template('SystemSite/selection.html')
    
    context = {
        'tourist_list': tourist_list,
        'operator_list': operator_list,
        'resultTourist' : "",
        'resultOperator' : ""
    }

    if request.method == 'POST' and 'lowerbound' in request.POST:
        lower_bound = request.POST['lowerbound']
        upper_bound = request.POST['upperbound']
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Tourist \
                            WHERE ArcadePoints >= %s AND ArcadePoints <= %s", [lower_bound, upper_bound])
            resultTourist = cursor.fetchall()
            context["resultTourist"] = resultTourist
        return HttpResponse(template.render(context, request))
    
    if request.method == 'POST' and 'qualification' in request.POST:
        qualification = request.POST['qualification']
        with connection.cursor() as cursor:
            cursor.execute("SELECT WorkID, op1.Qualification, RName FROM Operator_Operates_1 op1, Operator_Operates_2 op2 \
                            WHERE op1.Qualification = op2.Qualification  \
                            AND op1.Qualification LIKE %s", ["%" + qualification + "%"])
            resultOperator = cursor.fetchall()
            context["resultOperator"] = resultOperator
        return HttpResponse(template.render(context, request))
    

    return HttpResponse(template.render(context, request))

def nested_aggregation(request):
    tourist_joined_list = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT t.ID, t.Name, t.ArcadePoints, tb.TicketNo, t1.Type  \
                       FROM Tourist t, TouristBuysTicket tb, Ticket_1 t1 \
                       WHERE t.ID = tb.TID AND tb.TicketNo = t1.TicketNo")
        tourist_joined_list = cursor.fetchall()
    
    template = loader.get_template('SystemSite/nested_aggregation.html')
    
    context = {
        'tourist_joined_list': tourist_joined_list,
        'selection': "gt",
        'result' : ""
    }

    if request.method == 'POST':
        with connection.cursor() as cursor:
            if request.POST['Relation'] == "gt":
                context['selection'] = "gt"
                cursor.execute("""SELECT t1.Type, avg(t.ArcadePoints), count(*)   \
                            FROM Tourist t, TouristBuysTicket tb, Ticket_1 t1 \
                            WHERE t.ID = tb.TID AND tb.TicketNo = t1.TicketNo  \
                            GROUP BY t1.Type \
                            HAVING avg(t.ArcadePoints) > (SELECT avg(ArcadePoints) \
                                                        FROM Tourist)""")
            elif request.POST['Relation'] == "lt":
                context['selection'] = "lt"
                cursor.execute("""SELECT t1.Type, avg(t.ArcadePoints), count(*)   \
                            FROM Tourist t, TouristBuysTicket tb, Ticket_1 t1 \
                            WHERE t.ID = tb.TID AND tb.TicketNo = t1.TicketNo  \
                            GROUP BY t1.Type \
                            HAVING avg(t.ArcadePoints) < (SELECT avg(ArcadePoints) \
                                                        FROM Tourist)""")
            result = cursor.fetchall()
            context['result'] = result
        return HttpResponse(template.render(context, request))

# Join
def join(request):
    technician_list = view_table('Technician')
    staff_list = view_table('Staff')
    rideMaintains_list = view_table('Ride_Maintains')
    template = loader.get_template('SystemSite/join.html')
    with connection.cursor() as cursor:
        cursor.execute("SELECT t.WorkID, t.Qualification, s.Name, rm.RName,rm.PassengerLimit,rm.EID,rm.TimeofInspection FROM Technician t, Staff s, Ride_Maintains rm WHERE t.WorkID = s.WorkID AND s.WorkID=rm.WorkID")
        joined_list = cursor.fetchall()

    context = {
        'technician_list' : technician_list,
        'staff_list' : staff_list,
        'rideMaintains_list': rideMaintains_list,
        'joined_list': joined_list,
        'formJ': "",
        'aj_list': ""
    }    
    
    if request.method == 'POST':
        formJ = joinForm(request.POST)
        if formJ.is_valid():
                rName = formJ.cleaned_data['ride_name']
                with connection.cursor() as cursor:
                    cursor.execute("SELECT t.Qualification, s.Name FROM Technician t, Staff s, Ride_Maintains rm WHERE t.WorkID = s.WorkID AND s.WorkID=rm.WorkID AND rm.RName=%s", [rName])
                    aj_list = cursor.fetchall()
                context['aj_list'] = aj_list
                context['formJ'] = formJ
                return HttpResponse(template.render(context, request))
    else: 
        context['formJ'] = joinForm()

    return HttpResponse(template.render(context, request))


# Projection
def proj(request):
    template = loader.get_template('SystemSite/projection.html')
    with connection.cursor() as cursor:
        cursor.execute("SELECT r.GID, r.TID, t.Name,t.Age,t.ArcadePoints FROM Redeems r JOIN Tourist t ON t.ID = r.TID")
        joined_list = cursor.fetchall()
    context = {
        'joined_list': joined_list,
        'formP': "",
        'a1': "",
        'a2': "",
        'a3': "",
        'aj_list': ""
    } 
    dict_col = {
        "GID" : "Gift ID",
        "TID" : "Tourist ID",
        "Name": "Tourist Name",
        "Age": "Age",
        "ArcadePoints" : "Arcade Points"
    }

    if request.method == 'POST':
        formP = projForm(request.POST)
        if formP.is_valid():
                a1 = formP.cleaned_data['dropdown1']
                a2 = formP.cleaned_data['dropdown2']
                a3 = formP.cleaned_data['dropdown3']
                if a1 != a2 and a2 != a3:
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT %s, %s, %s FROM Redeems r JOIN Tourist t ON t.ID = r.TID" % (a1, a2, a3))
                        aj_list = cursor.fetchall()
                    context['aj_list'] = aj_list
                    context['a1'] = dict_col[a1]
                    context['a2'] = dict_col[a2]
                    context['a3'] = dict_col[a3]
                context['formP'] = formP
                return HttpResponse(template.render(context, request))
    else: 
        context['formP'] = projForm()
    return HttpResponse(template.render(context, request))

# Aggregation with group by
def groupby(request):
    template = loader.get_template('SystemSite/agroupby.html')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Ticket_1 NATURAL LEFT OUTER JOIN TicketForRide")
        joined_list = cursor.fetchall()
        
    context = {
        'joined_list':joined_list,
        'aq_list':""
    } 
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("SELECT Type, COUNT(distinct RideName) FROM Ticket_1 NATURAL LEFT OUTER JOIN TicketForRide GROUP BY Type")
            context['aq_list'] = cursor.fetchall()
    return HttpResponse(template.render(context, request))

def view_table(name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM " + name)
        table = cursor.fetchall()
    return table

def view_table_natural_join(names):
    with connection.cursor() as cursor:
        joinedstr = " NATURAL JOIN ".join(names)
        cursor.execute("SELECT * FROM " + joinedstr)
        table = cursor.fetchall()
    return table



