#-*- coding: utf-8 -*-
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50,verbose_name="Imie")
    date_of_birth = models.DateField(verbose_name="Data urodzenia")
    email = models.EmailField(verbose_name="Adres e-mail")
    height = models.IntegerField(verbose_name="Wzrost", default=170)

    def __str__(self):
        return self.name + " " + self.email


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nazwa")
    description = models.CharField(max_length=1000, verbose_name="Opis")
    client = models.CharField(max_length=1000, verbose_name="Klient")

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nazwa")
    description = models.CharField(max_length=1000, verbose_name="Opis")
    time_elapsed = models.IntegerField(verbose_name="Przepracowany czas" , null=True, default=None, blank=True)
    project = models.ForeignKey(Project, verbose_name="Projekt" , null=True, default=None, blank=True)
    app_user = models.ForeignKey(Person, verbose_name="Wykonawca")
    
    def __str__(self):
        return self.title

class Supervisor(Person):
    specialisation = models.CharField(max_length=50, verbose_name="Specjalizacja")


class Developer(Person):
    supervisor = models.ForeignKey(Supervisor, verbose_name="Przelozony")
# Create your models here.