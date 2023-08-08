"""

Admin and Authentication
Admin Account

In an earlier lesson, we explored one of Django’s most powerful features, the admin interface.
The admin interface is a management tool that gives us control of creating, updating, reading, and deleting records from our database.
This makes it very easy to test our models and ensure that we’re retrieving or creating data correctly.

In order to access the Admin interface, we must first programmatically create a superuser.
In Django, a superuser has the permissions to freely control data.
To create a superuser, we can type the following command in our terminal:
"""
python3 manage.py createsuperuser

"""
The shell will prompt us to type in a username, email, and password.
Once completed, we can navigate to the /admin route and log in with the credentials we just used to create our superuser.
If we get redirected to the index page, that means our login was successful!

It’s imperative to not share this information with anyone since the admin account has complete control of all your records in the database.
In case you forget your admin username you can always reset through the User object.
Instructions
1.

Let’s start by creating a superuser!

In the terminal, type the command to create a superuser. Use the following credentials:

    Username: admin
    Email: admin@vetoffice.com
    Password: admin123

Once you run the command and create a new superuser, click on “Check Work” to make sure you added the correct input.

NOTE: When entering the password, you will be warned that the password and username are too similar. Bypass this warning by typing y.
Checkpoint 2 Passed

You can start a python shell with the following command:
"""
python3 manage.py createsuperuser
 """

2.

Run the application and navigate to the admin interface. Log in with your created credentials.
Checkpoint 3 Passed

Make sure to use the proper credentials!


"""
