from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm
# Import logout below:
from django.contrib.auth import logout

# Add your logout function below:
def logout_view(request):
  logout(request)
  return redirect("home")

@login_required
def home(request):
   context = {"name": request.user.username}
   return render(request, "vetoffice/home.html", context)

class OwnerList(LoginRequiredMixin, ListView):
   model = Owner

class PatientList(LoginRequiredMixin, ListView):
    model = Patient

class OwnerCreate(LoginRequiredMixin, CreateView):
   model = Owner
   template_name = "vetoffice/owner_create_form.html"
   form_class = OwnerCreateForm

class PatientCreate(LoginRequiredMixin, CreateView):
    model=Patient
    template_name = "vetoffice/patient_create_form.html"
    form_class = PatientCreateForm

class OwnerUpdate(LoginRequiredMixin, UpdateView):
   model = Owner
   template_name = "vetoffice/owner_update_form.html"
   form_class = OwnerUpdateForm

class PatientUpdate(LoginRequiredMixin, UpdateView):
   model = Patient
   template_name = "vetoffice/patient_update_form.html"
   form_class = PatientUpdateForm

class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"
    success_url = "/owner/list"

class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"
    success_url = "/patient/list"
