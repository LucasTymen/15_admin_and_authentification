"""

Admin and Authentication
User Objects

We’ve seen how powerful Django’s admin interface is in order to manipulate records in our database.
However, this is not the only way!

In the shell, we can manage our users programmatically using one of the core objects in Django’s authentication system, the User object.
==> https://docs.djangoproject.com/en/4.1/topics/auth/default/#user-objects

The object can be imported from django.contrib.auth.models and comes with a number of helper methods including one to create users, .create_user().
==> https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user

This method can take a username, email, and password as arguments:
"""

user = User.objects.create_user(username="myusername", email="myemail@crazymail.com", password="mypassword")

"""
The .create_user() method will automatically create and save the user to the database.
We also gain a security feature because this method also automatically hashes the password so it’s not stored as a plain string value in the database.
==> https://en.wikipedia.org/wiki/Cryptographic_hash_function

Moreover, we can call the .save() method in order to save the user object back to the database if we make any further changes.

Moreover, the User object also contains other primary attributes such as:
first_name, last_name, email, username, and password.
Additionally, we can handle a wide range of tasks from updating a user’s email address, to changing their password or even deleting a user.

Note: When working with the Python shell, if you want to exit at any time you can type Ctrl+Z on Windows, Ctrl+D on Mac or type and run exit().
Instructions
1.

In the terminal, open the Python shell and import the User object. After you enter the required commands, hit Run to move to the next step.

    Note: If your screen size doesn’t allow for the commands to fit on a single line, the tests in this exercise may fail.
    To ensure that tests are working properly, please stretch out the length of the Terminal to fit any commands into a single line.

To open the Python shell use the command:
"""

python3 manage.py shell

"""
Import the user with the following line:
"""

from django.contrib.auth.models import User

"""
2.

Create a new user object with the following attributes:

    Username: "tom100"
    Email: "tom@codecademy.com"
    Password: "codec@demy123"

Store the user in a variable called user. Once created, make sure to save the user variable in the database.

When calling the .create_user() method, make sure you add the arguments in order. See the following syntax as a reminder.
Note: please also expand your terminal to allow for your command to be written in a single line.
"""

user = User.objects.create_user(username="username", email="email@example.com", password="password")

"""
You can then save the user with the .save() command:
"""
user.save()

"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
