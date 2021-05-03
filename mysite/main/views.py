from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddApplicationForm
from .models import Application, Level, Role, Status


def home(request):
    return render(request, "home.html")

"""
display all applications
"""
def view(request):
    levels = Level.objects.all()
    roles = Role.objects.all()
    statuses = Status.objects.all()
    if request.method == "POST":
        applications = Application.objects.filter(
            company__contains=request.POST["company_filter"],
            role__role__contains=request.POST["role_filter"],
            level__level__contains=request.POST["level_filter"],
            status__status__contains=request.POST["status_filter"])
        if request.POST["order_filter"] == "newest_first":
            applications = applications.order_by("-date_applied")
        else:
            applications = applications.order_by("date_applied")
        return render(request, "view.html", context= {"applications":applications, "levels":levels, "roles":roles, "statuses":statuses})
    applications = Application.objects.all().order_by("-date_applied")
    return render(request, "view.html", context= {"applications":applications, "levels": levels, "roles":roles, "statuses":statuses})

"""
take values of user input in form and add them to the database
"""
def add_entry(request):
    if request.method == "POST":
        form = AddApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:view")

    form = AddApplicationForm()
    return render(request, "add.html", context={"form": form})


"""
process an input with the name "application_id" and use it
to delete an entry in the Application table with the corresponding pk.
"""
def delete_entry(request):
    if request.method == "POST":
        application = Application.objects.get(id=request.POST["application_id"])
        application.delete()
    return redirect("main:view")

#i'd prefer to not send a pk via url
def edit_entry(request, pk):
    application = Application.objects.get(id=pk)
    if request.method == "POST":
        form = AddApplicationForm(request.POST, instance=application)
        if form.is_valid:
            form.save()
        return redirect("main:view")
    form = AddApplicationForm(instance=application)
    return render(request, "edit.html", context={"form":form})

