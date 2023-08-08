"""

Admin and Authentication
Log In

After a user object is created, they can use those credentials to log in to gain access to the site. In order to log in a user, we can make use of the login() function provided by Django:

# views.py
From django.contrib.auth import login

def login_view(request):
  # ... Other code
  login(request, user)


In order to make use of login(), we must first import it from django.contrib.auth. The function takes in a request object followed by a user object. If a user is successfully logged in, a session will be created. But what exactly is a session?

In Django, once the user has been logged in to their account, and until they log out on that device, they are having a session. With Django’s session framework, sessions are used to abstract the receiving and sending of cookies. While data is saved on the server-side, the session created uses a cookie containing a special session id to identify each browser and its associated session with the site. This allows us to keep track of the user as they navigate around the site without constantly needing them to log in.

Using our example from the previous lesson, we can see what the proper flow is of logging in a user:

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def login_view(request):
  username = request.POST["username"]
  password = request.POST["password"]

  user =  authenticate(request, username=username, password=password)

  # Check if a user is verified and authenticated
  if user is not None:
    # Use the returned user object in login()
    login(request, user)

    # Redirect to home page after logging in
    return redirect("home.html")
  else:
    render(request, "registration/login.html", context)


The main difference is that in our if statement, we’re now able to create a session by calling login() using request and our created user object.
Instructions
1.

Our code block to sign in users is currently incomplete, add the login() function in order to log in a user after they’re authenticated.

Make sure to add login() within your if statement:

# Other login_view code...
  if user is not None:
    login(request, user)
    return redirect("dashboard.html")
  else:
    render(request, "registration/login.html", context)


2.

In the mini-browser, navigate to account/login and attempt to log in with valid credentials:

    Username: tom100
    Password: codec@demy123

Notice that tom100 is displayed in the browser! Look over the home() view function to see what change was needed to make this display happen.

The log in page should re-render with empty fields if you attempt to log in with invalid credentials!

The change in home() was that we’re not hard coding context‘s "name" value. Instead, we’re using request.user since we have that credential stored!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
