from django import forms

class NameForm(forms.Form):
    ID = forms.IntegerField(label = 'ID')
    Name = forms.CharField(label = 'Name', max_length = 100)
    Age = forms.IntegerField(label = 'Age')
    Arcadept = forms.IntegerField(label = 'Arcade Pts')
