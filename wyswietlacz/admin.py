from django.contrib import admin

from .models import Person, Project, Task, Supervisor, Developer

admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Supervisor)
admin.site.register(Developer)
# Register your models here.
