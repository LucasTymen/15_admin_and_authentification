"""

Admin and Authentication
Registering Tables in Admin

Now that we have access to the admin interface, let’s explore how we can use it to interact with our database records.

Consider an application that keeps track of all the books we’ve read.
Within our application, we have a model called Book that holds information about each book (title, author, date of publication, etc).

In order to be able to interact with a database table through the admin interface, we first need to register the model.
Registering and configuring a model is done by adding the models into the app’s admin.py file.

"""
# myapp_root/book_catalog/admin.py

from .models import Book

admin.site.register(Book)
 """


Notice that we’ve first imported the Book model. Then we called the register() method:
==> https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site#registering_models
"""

admin.site.register(Book)

"""
After we save our admin.py file, the /admin route will display our registered model, Book.
If we registered more models, they would be grouped by the installed application.

From the /admin page, we can click on the collection of Books and we’ll be directed to a table that shows us all the information and records held in this database table.
Now we’re able to manually create, update, read, or delete any record using the admin interface!

Note: It’s important to remember that the admin interface is not something to be shared with any user.
We wouldn’t want all of our users to have access to the interface and manipulate records as they wish!
Instructions
1.

Let’s make sure we can interact with our Owner and Patient models within the Admin interface!

Start by importing the models Owner and Patient in /vetoffice/admin.py.

The models can be imported from .models:

from .models import Employee


2.

Once imported register both models to the admin interface using the register() method.

The register() can be accessed through dot notation:

admin.site.register(Inventory)


3.

In the admin interface, login with the admin user credentials (username: admin, password: admin123) and make sure the tables are populated.

Using the admin interface, you can manipulate the model instances using any CRUD functionality!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
==> https://www.codecademy.com/learn/paths/build-python-web-apps-with-django/tracks/accounts-and-authentication-in-django/modules/django-accounts-and-authentication/cheatsheet
"""
