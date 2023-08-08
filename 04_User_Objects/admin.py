from django.contrib import admin
from .models import Owner, Patient
from django.contrib.auth.models import User

admin.site.register(Owner)
admin.site.register(Patient)

user = User.objects.create_user(username="tom100", email="tom@codecademy.com", password="codec@demy123")

user.save()
