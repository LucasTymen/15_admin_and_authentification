"""

Admin and Authentication
Authenticating Users

We know that authenticating a user entails matching credentials sent from the client against the server’s stored data.
If the information matches, then access will be granted.

The process of authenticating a user is all done on the server-side of our applications.
To be more specific, we can add this logic in a view function that will accept credentials and make use of the authenticate() function to verify a user.
==> https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.authenticate

authenticate() takes credentials as keyword arguments, with username and password for the default case.
If the credentials are valid, a User object will be returned, otherwise, a PermissionDenied exception is raised which returns None.
==> https://docs.djangoproject.com/en/4.1/ref/exceptions/#permissiondenied

We can capture the fields from a log in form with request.POST, which is a dictionary-like object that lets you access submitted data by key name.
If we have a field for username, we can retrieve that value with request.POST["username"].

Let’s break down how this function would work:
"""

from django.contrib.auth import authenticate

def login_view(request):
  # Both username and password are captured from the submitted log in form
  username = request.POST["username"]
  password = request.POST["password"]

  # Both username and password are passed into the authenticate() method to verify the user
  user = authenticate(request, username=username, password=password)

  # If the user is valid, then a user object is returned.
  if user is not None:
    # Log in user and redirect them
    return redirect("home.html")
  else:
    return HttpResponse("Invalid credentials!")

"""
In the code above we first import authenticate from the auth library provided by Django.
We then store the values of our username and password provided from the log in form with request.POST into variables, username and password respectively.

Once those values are stored in variables, we can then pass them as arguments into the authenticate function:
"""

authenticate(request, username=username, password=password)

"""
For best practices, we make use of an if/else statement to check if the user was authenticated successfully.
This allows us to handle any exceptions in case an unauthenticated user tries to log in.
If the credentials were valid, and a User object is returned, we can log them in (we’ll look into this in the next lesson) and redirect them to a new page.

Notice how we’re making use of a handy function provided by Django, redirect().
This function is imported from django.shortcuts and allows us to redirect a user to a specific view by passing in the name of a view.
==> https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#redirect

Otherwise, the else code block is executed and sends an HttpResponse with the text “Invalid credentials!”`.

With just a few lines of code, Django allows us to authenticate users seamlessly!
Instructions
1.

We’ve provided you with a login method, however, the logic to log in users is incomplete.

Add the authenticate() method with username and password as arguments.

Make sure to store the result in a variable called user.

Your authenticate method should look as follows:
"""

user = authenticate(request, username=username, password=password)

"""
2.

Within the mini-browser attempt to log in with the user credentials from the previous lesson:

    Username: tom100
    Password: codec@demy123

Make sure to run and check your work before attempting to log in!

If your mini-browser is showing blank, refresh the page to see the log in page.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
