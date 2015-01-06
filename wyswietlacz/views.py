from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import *
from forms import *

def projects(request):
    all_projects = Project.objects.all()
    context = {'action': "Show projects", 'all_projects': all_projects}
    return render(request, 'projects.html', context)

def choice(request):
    action='Projekty dla klienta "Ja"'
    all_projects = Project.objects.filter(client="Ja")
    return render(request, 'choice.html', locals())

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    tasks = Task.objects.filter(project = project)
    return render(request, 'project_detail.html', locals())

def developers(request):
    all_developers = Developer.objects.all()
    context = {'all_developers': all_developers}
    return render(request, 'developers.html', context)

def createdev(request):
    if request.method == "POST":
        form = DeveloperForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date_of_birth = form.cleaned_data['date_of_birth']
            supervisor = form.cleaned_data['supervisor']
            height = form.cleaned_data['height']
            new_developer = Developer(name=name, email=email, date_of_birth=date_of_birth, height=height, supervisor=supervisor)
            new_developer.save()
            return HttpResponseRedirect('/wyswietlacz/developers/')
        else:
            return render(request, 'create_developer.html', {'form' : form})
    else:
        form = DeveloperForm()
    return render(request, 'create_developer.html', {'form' : form})

def createproject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            client = form.cleaned_data['client']
            new_project = Project(title=title, description=description, client=client)
            new_project.save()
            return HttpResponseRedirect('/wyswietlacz/projects/')
        else:
            return render(request, 'create_project.html', {'form' : form})
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form' : form})

def tasks(request):
    all_tasks = Task.objects.all()
    context = {'all_tasks': all_tasks}
    return render(request, 'tasks.html', context)

def createtask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            time_elapsed = form.cleaned_data['time_elapsed']
            project = form.cleaned_data['project']
            app_user = form.cleaned_data['app_user']
            new_task = Task(title=title, description=description, time_elapsed=time_elapsed, project=project, app_user=app_user)
            new_task.save()
            return HttpResponseRedirect('/wyswietlacz/tasks/')
        else:
            return render(request, 'create_task.html', {'form' : form})
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form' : form})
# Create your views here.
