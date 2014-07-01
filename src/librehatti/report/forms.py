from django import forms
#from search_choices import CLIENT_FIELD_CHOICES,CLIENT_ORDER_CHOICES, CLIENT_ORDER_TYPES_CHOICES
#from search_choices import JOB_SEARCH_CHOICES
from search_choices import *
import datetime


class ClientForm(forms.Form):
        client_fields = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=CLIENT_FIELD_CHOICES)
        
       
        
        
class OrderForm(forms.Form):
        order = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=CLIENT_ORDER_CHOICES)


        
class AddConstraints(forms.Form):
       
        start_date = forms.DateField(required=False, initial='2014-01-01')
        end_date = forms.DateField(required=False, initial= datetime.date.today())
        additional_constraints =  forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices= CONSTRAINT_CHOICES)
        amount_greater_than = forms.FloatField(required=False, initial = 0)
        amount_less_than = forms.FloatField(required=False, initial = 1000000)
