from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Import your decorators and mixins below

from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm

# Add the login_required decorator:

def home(request):
   context = {"name": "Django-er"}
   return render(request, "vetoffice/home.html", context)

# Add the LoginRequiredMixin:
class OwnerList(ListView):
   model = Owner

# Add the LoginRequiredMixin:
class PatientList(ListView):
    model = Patient

# Add the LoginRequiredMixin:
class OwnerCreate(CreateView):
   model = Owner
   template_name = "vetoffice/owner_create_form.html"
   form_class = OwnerCreateForm

# Add the LoginRequiredMixin:
class PatientCreate(CreateView):
    model=Patient
    template_name = "vetoffice/patient_create_form.html"
    form_class = PatientCreateForm

# Add the LoginRequiredMixin:
class OwnerUpdate(UpdateView):
   model = Owner
   template_name = "vetoffice/owner_update_form.html"
   form_class = OwnerUpdateForm

# Add the LoginRequiredMixin:
class PatientUpdate(UpdateView):
   model = Patient
   template_name = "vetoffice/patient_update_form.html"
   form_class = PatientUpdateForm

# Add the LoginRequiredMixin:
class OwnerDelete(DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"
    success_url = "/owner/list"

# Add the LoginRequiredMixin:
class PatientDelete(DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"
    success_url = "/patient/list"
