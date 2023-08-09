from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Import your decorators and mixins below
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm

# Add the login_required decorator:
@login_required
def home(request):
   context = {"name": "Django-er"}
   return render(request, "vetoffice/home.html", context)

# Add the LoginRequiredMixin:
class OwnerList(LoginRequiredMixin ,ListView):
   model = Owner

# Add the LoginRequiredMixin:
class PatientList(LoginRequiredMixin, ListView):
    model = Patient

# Add the LoginRequiredMixin:
class OwnerCreate(LoginRequiredMixin, CreateView):
   model = Owner
   template_name = "vetoffice/owner_create_form.html"
   form_class = OwnerCreateForm

# Add the LoginRequiredMixin:
class PatientCreate(LoginRequiredMixin, CreateView):
    model=Patient
    template_name = "vetoffice/patient_create_form.html"
    form_class = PatientCreateForm

# Add the LoginRequiredMixin:
class OwnerUpdate(LoginRequiredMixin, UpdateView):
   model = Owner
   template_name = "vetoffice/owner_update_form.html"
   form_class = OwnerUpdateForm

# Add the LoginRequiredMixin:
class PatientUpdate(LoginRequiredMixin, UpdateView):
   model = Patient
   template_name = "vetoffice/patient_update_form.html"
   form_class = PatientUpdateForm

# Add the LoginRequiredMixin:
class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"
    success_url = "/owner/list"

# Add the LoginRequiredMixin:
class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"
    success_url = "/patient/list"
