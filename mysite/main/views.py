from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddApplicationForm

#views
def home(request):
    if request.method == "POST":
        pass
    return render(request, "home.html")

def add_entry(request):
    if request.method == "POST":
        form = AddApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:home")

    form = AddApplicationForm()
    return render(request, "add.html", context={"form": form})

