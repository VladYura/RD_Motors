from django import forms
from django_select2.forms import Select2Widget
from django_select2 import forms as s2forms
from .models import PartCard, Category, Cars


class MainForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, widget=Select2Widget)
    car = forms.ModelChoiceField(queryset=Cars.objects.all(), required=False, widget=Select2Widget)
    car_year = forms.IntegerField(required=False)
    article = forms.CharField(required=False)
