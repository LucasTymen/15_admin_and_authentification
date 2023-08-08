from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm

def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    # Add your code below:
    user = authenticate(request, username=username, password=password)
    if user is not None:
      return redirect("home")
    else:
      return HttpResponse("invalid credentials")
  return render(request, "registration/login.html", context)


def home(request):
   context = {"name": "Django-er"}
   return render(request, "vetoffice/home.html", context)

class OwnerList(ListView):
   model = Owner

class PatientList(ListView):
    model = Patient

class OwnerCreate(CreateView):
   model = Owner
   template_name = "vetoffice/owner_create_form.html"
   form_class = OwnerCreateForm

class PatientCreate(CreateView):
    model=Patient
    template_name = "vetoffice/patient_create_form.html"
    form_class = PatientCreateForm

class OwnerUpdate(UpdateView):
   model = Owner
   template_name = "vetoffice/owner_update_form.html"
   form_class = OwnerUpdateForm

class PatientUpdate(UpdateView):
   model = Patient
   template_name = "vetoffice/patient_update_form.html"
   form_class = PatientUpdateForm

class OwnerDelete(DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"
    success_url = "/owner/list"

class PatientDelete(DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"
    success_url = "/patient/list"
