"""

Admin and Authentication
Logging Out

Django’s built-in functions make logging out a user a painless process.

The logout() function takes in a requestand returns None:
"""

# views.py

def logout_view(request):
  # ... Other logic
  logout(request)
  return redirect("home")

"""
By calling the logout() function we completely delete the session data that was associated with the logged in user.
It is important to note that calling the logout() function doesn’t throw any errors if the user is not logged in.
Once the logout function is called, we can then redirect the user to a different view page by using redirect().
==> https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/#redirect

We can then add a new path to logout our users in our app’s urls.py:
"""

urlpatterns = [
  path("/logout", logout, name="logout")
]

"""
Once a user is directed to that route, they will be logged out and their session will be destroyed.
Instructions
1.

In views.py, let’s start by importing the logout function from django.contrib.auth.
2.

We’ve learned how to log in users, let’s allow them to log out!

Create a new logout view function, logout_view().

Inside the function block, make a call to logout(request).

Once a user logs out, let’s use the redirect() function to send the user to the "home" template!

Remember to pass in request as an argument!
"""

def logout_view(request):
  logout(request)
  return redirect("home")

"""
Notice that since we’re using our login decorators on the "home" template, the user will be required to login to access it!
3.

Now we need to access the logout view within our home page.

    Add the created logout_view function into your urls.py file.
    Set the path to "logout/".
    Assign "logout" to the name attribute.

The view function has been imported, make sure you used the right syntax.
"""

urlpatterns = [
  path("/sample", views.sample, name="sample")
]

"""
4.

Attempt to log in and then log out within the mini-browser.

Here are the credentials:

    Username: tom100
    Password: codec@demy123

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
==> https://www.codecademy.com/learn/paths/build-python-web-apps-with-django/tracks/accounts-and-authentication-in-django/modules/django-accounts-and-authentication/cheatsheet
"""
