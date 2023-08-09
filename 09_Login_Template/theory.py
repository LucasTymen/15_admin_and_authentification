"""

Admin and Authentication
Login Template

We’ve made great progress writing functions to log users in and out of our site, let’s now explore how to make use of these functions in our view pages.

By default, the login() view function provided by Django will try to render the registration/login.html template.
So the basic configuration would be creating a folder named registration/ and placing a login.html template inside:
"""

<!-- registration/login.html -->

{% block title %}Login{% endblock %}

{% block content %}
  <h2>Login</h2>
    <form method="post">
      {% csrf_token %}
      <table>
        {{ form.as_p }}
        <tr>
          <td>&nbsp;</td>
          <td><input type="submit" value="Submit"></td>
        </tr>
      </table>
    </form>
{% endblock %}

"""
In the code above, we’re making sure that our form sends a POST request to the server.
The value of the form template variable will be provided by the login() view which allows the form’s fields and their attributes to be unpacked into HTML markup.
We also use form.as_p in order to wrap all the elements of our form in HTML <p> tags.
By using form.as_p we can avoid writing a loop in the template to explicitly add HTML to surround each title and field.
Django is able to know what fields are required to create or log in a user and automatically renders these fields for us.
Not only that, but we also are provided with validation errors in case a user logs in with invalid credentials!

For more rendering options using the form template, feel free to take a look at the main documentation.
==> https://docs.djangoproject.com/en/4.1/topics/forms/#working-with-form-templates

Instructions
1.

Let’s see how the fields are automatically rendered for us using Django’s built-in methods.

Add the form.as_p method within registration/login.html.

Remember to wrap the method call within two curly brackets and to add it within the <form> tags:
"""

<form>
  ...
  {{ form.as_p }}
</form>

"""
2.

In the mini-browser, you’re already on the /account/login page. Attempt to log in with invalid credentials to see the warnings rendered on the page.

The mini-browser might load up with the validdation errors already displayed for you. Take a look at everything Django automatically verifies for us!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
