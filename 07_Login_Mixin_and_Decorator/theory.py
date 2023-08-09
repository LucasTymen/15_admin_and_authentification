"""

Admin and Authentication
Login Mixin and Decorator

We have looked at how to implement the logic to authorize and log in users to give them access to our site.
But, the truth is Django actually handles a lot of this logic for us!
That’s right, we took the hard route implementing that logic ourselves.
Now, let’s take the easy route by getting acquainted with Django’s “batteries included” means of authenticating and authorizing users to access specific pages.
Introducing mixins, a type of class that is used to “mix in” extra properties and methods into another class.
One mixin that Django provides is the LoginRequiredMixin.

In order to use the LoginRequiredMixin we need to import it from django.contrib.auth.mixins:
"""

# views.py
from django.contrib.auth.mixins import LoginRequiredMixin

"""
When using class-based views, we can pass a mixin as an argument.
It’s important to note that mixins are called in order from left to right so we’ll want to add the login mixin before the view:
"""

# views.py
class SomeView(LoginRequiredMixin, ListView):
  model = ModelExample

"""
By implementing the LoginRequiredMixin, Django takes care of the whole process of authenticating users and making sure they’re verified before rendering a specific page.

Aside from the mixin, Django also provides us with decorators.
A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
In order to use it, we must first import it into our file and add the line @login_required on top of the function we want to extend:
"""

# views.py
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
  return render(request, "app/profile.html", name="profile")

"""
Using the decorator, we’re able to deny access to a view if the user is not logged in.
With just one line, Django is able to take care of all the logic required to deny/allow access to specific pages!

Both the login mixin and decorator do roughly the same thing.
The main difference lies in the syntax and implementation — mixins are used for classes, while decorators are used for functions.
Instructions
1.

In its current state, any user can navigate through the site without logging in.

Let’s change that by first importing the login_required decorator at the top of views.py

You can import the decorator from django.contrib.auth.decorators:

from django.contrib.auth.decorators import login_required


2.

Add the login_required decorator to the home() view function.

Once implemented, attempt to navigate through the home page, you should now be required to log in to access it.

The login_required decorator can be added above your function definition and prepending it with the @ symbol:
"""

@login_required
def view_func(request):
  # ... Function body

    """
3.

Let’s add a little more security and make use of the LoginRequiredMixin. Start by importing the mixin at the top of your views.py file.

You can import theLoginRequiredMixedin from django.contrib.auth.mixins:

from django.contrib.auth.mixins import LoginRequiredMixin


4.

Now we can make use of the LoginRequiredMixin!

In each of your class-based views, add the mixin as the first argument.

Make sure you’re adding the mixin as the first argument!

class BookList(LoginRequiredMixin, ListView)


5.

Now when you try to view any of the pages, you’ll need to log in.

Log in with the credentials to view the pages again:

    Username: tom100
    Password: codec@demy123

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
