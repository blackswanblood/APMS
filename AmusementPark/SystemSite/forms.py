from django import forms

class NameForm(forms.Form):
    ID = forms.IntegerField(label = 'ID')
    Name = forms.CharField(label = 'Name')
    Age = forms.IntegerField(label = 'Age')
    Arcadept = forms.IntegerField(label = 'Arcadept')
