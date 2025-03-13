
from django import forms
from.models import stationdetails

class mapitem(forms.ModelForms):
    class Meta:
        model = stationdetails
        fields = ['name', 'latitude', 'longitude']