from django import forms
from django.forms.extras.widgets import SelectDateWidget
from models import *

BIRTH_YEAR_CHOICES = range(1900,2015)

class DeveloperForm(forms.Form):

    name = forms.CharField(label="Imie", max_length=30)
    email = forms.CharField(label="e-mail", max_length=30)
    date_of_birth = forms.DateField(label="urodzony", widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    height = forms.IntegerField(label="wzrost")
    supervisor = forms.ModelChoiceField(label="Szef", queryset=Supervisor.objects.all())

class ProjectForm(forms.Form):

    title = forms.CharField(max_length=50, label="Nazwa")
    description = forms.CharField(max_length=1000, label="Opis")
    client = forms.CharField(max_length=1000, label="Klient")
    
class TaskForm(forms.Form):

    title = forms.CharField(max_length=50, label="Nazwa")
    description = forms.CharField(max_length=1000, label="Opis")
    time_elapsed = forms.IntegerField(label="Przepracowany czas")
    project = forms.ModelChoiceField(label="Projekt", queryset=Project.objects.all())
    app_user = forms.ModelChoiceField(label="Wykonawca", queryset=Developer.objects.all())

