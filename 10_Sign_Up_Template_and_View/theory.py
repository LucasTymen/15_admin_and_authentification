"""

Admin and Authentication
Sign Up Template and View

Now that we can log users in and out, let’s see how we can register new users using a signup form.
A straightforward way of creating a signup page is by using UserCreationForm and the CreateView class-based view which are both provided by Django.

Here’s how a sign up class-based view could look like:
"""

# views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

"""
Our SignUp class is using a CreateView class, in which we can specify what information to include.

    The first thing we’ll set is the form_class as a UserCreationForm which will generate the necessary fields for us (username and password).
        The UserCreationForm was imported from django.contrib.auth.forms
        ==> https://docs.djangoproject.com/en/3.1/ref/urlresolvers/#reverse-lazy

    Afterward, we use the success_url attribute to assign a URL to redirect the signed up user
        We use the reverse_lazy() method to generate a full URL from a name.
        We set the successful redirect to go to "login" path since we still want a user to login.
    Lastly, we’ll assign "registration/signup.html" to template_name so we can render that specific template.

Having set up our view class, we need to add the view into urls.py. Remember to call .as_view() whenever you work with class-based views:
"""

# urls.py

path("signup/", views.SignUp.as_view(), name="signup"),

"""
Since your signup template is making use of the form.as_p function, whenever a user tries to register with invalid credentials Django is versatile enough to provide any warnings or validation errors automatically!
==> https://docs.djangoproject.com/en/3.1/topics/auth/default/#all-authentication-views


We can apply similar authentication views into our login and logout process as well! For more information on these views, refer to the documentation.
Instructions
1.

Let’s allow new users to register to our app!

We’ve helped import the forms, the reverse_lazy() function, and provided you with a SignUp class-based view. But it’s missing a few key pieces.

    Add the form_class attribute and assign it to UserCreationForm.
    Add a success_url attribute and assign it to reverse_lazy("login").
    Add a template_name attribute and assign it to "registration/signup.html".

Your SignUp form should look as follows:
"""

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

"""
2.

Let’s add a new path for users to signup.

    Create a new path in urls.py, set the path name to "signup/".
    Add your newly created SignUp class-based view as the second argument.
    Assign "signup" to the name attribute.

Remember that class-based views are callable through the use of the .as_view() function:
"""

path("checkout/", views.Checkout.as_view(), name="checkout"),

"""
3.

Refresh your mini-browser and navigate to /signup in order to see your new signup form.

Attempt to sign up a new user and then log in with the new credentials.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
==> https://www.codecademy.com/learn/paths/build-python-web-apps-with-django/tracks/accounts-and-authentication-in-django/modules/django-accounts-and-authentication/cheatsheet
"""
