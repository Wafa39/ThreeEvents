from django import forms
from .models import Events


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events 
        fields = ['categoryname', 'pakagetype', 'pakagedetails', 'price']
        
    categoryname = forms.CharField(
        max_length=100,
        required=True,
        label=' Event name',
        
       
    )
    pakagetype = forms.CharField(
        max_length=100,
        required=True,
        label='Pakage Type'
    )
    
    pakagedetails = forms.CharField(
        required=True,
        min_value= 1,
        max_value = 1000,
        label='Pakage Details'
    )
    
    price = forms.FloatField(
        required=True,
        label="Price"
    )
        
    