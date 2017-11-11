from django import forms
from .models import Restaurant

class RestaurantNew(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name','owner','adress','speciality','fund_date']
    # name = forms.CharField(label='Name', max_length=200)
    # owner = forms.CharField(label='Owner', max_length=200)
    # adress = forms.CharField(label='Adress', max_length=200)
    # speciality = forms.CharField(label='Speciality', max_length=200)
    # fund_date = forms.DateField(label='Fundation Date')
