from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddApplicationForm
from .models import Application

#views
def home(request):
    applications = Application.objects.all()
    return render(request, "home.html", context= {"applications":applications})

def add_entry(request):
    if request.method == "POST":
        form = AddApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:home")

    form = AddApplicationForm()
    return render(request, "add.html", context={"form": form})


def delete_entry(request):
    if request.method == "POST":
        application = Application.objects.get(id=request.POST["application_id"])
        application.delete()
    return redirect("main:home")

