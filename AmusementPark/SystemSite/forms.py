from django import forms
import datetime

class NameForm(forms.Form):
    ID = forms.IntegerField(label = 'ID')
    Name = forms.CharField(label = 'Name', max_length = 100)
    Age = forms.IntegerField(label = 'Age')
    Arcadept = forms.IntegerField(label = 'Arcade Pts')

class MaintainanceForm(forms.Form):
    RideName = forms.CharField(label = 'Ride Name', max_length = 100)
    WorkID = forms.IntegerField(label = 'Work ID')
    EquipmentID = forms.IntegerField(label = 'Equipment ID')
    TOI = forms.DateField(label = 'Time of Inspection', initial=datetime.date.today)
