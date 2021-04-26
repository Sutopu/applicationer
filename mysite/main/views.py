from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddApplicationForm
from .models import Application


def home(request):
    return render(request, "home.html")

"""
display all applications
"""
def view(request):
    applications = Application.objects.all()
    return render(request, "view.html", context= {"applications":applications})

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

