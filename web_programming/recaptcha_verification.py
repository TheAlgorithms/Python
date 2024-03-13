"""
Recaptcha is a free captcha service offered by Google in order to secure websites and
forms.  At https://www.google.com/recaptcha/admin/create you can create new recaptcha
keys and see the keys that your have already created.
* Keep in mind that recaptcha doesn't work with localhost
When you create a recaptcha key, your will get two separate keys: ClientKey & SecretKey.
ClientKey should be kept in your site's front end
SecretKey should be kept in your site's  back end

# An example HTML login form with recaptcha tag is shown below

    <form action="" method="post">
        <h2 class="text-center">Log in</h2>
        {% csrf_token %}
        <div class="form-group">
            <input type="text" name="username" required="required">
        </div>
        <div class="form-group">
            <input type="password" name="password" required="required">
        </div>
        <div class="form-group">
            <button type="submit">Log in</button>
        </div>
        <!-- Below is the recaptcha tag of html -->
        <div class="g-recaptcha" data-sitekey="ClientKey"></div>
    </form>

    <!-- Below is the recaptcha script to be kept inside html tag -->
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

Below a Django function for the views.py file contains a login form for demonstrating
recaptcha verification.
"""

import requests

try:
    from django.contrib.auth import authenticate, login
    from django.shortcuts import redirect, render
except ImportError:
    authenticate = login = render = redirect = print


def login_using_recaptcha(request):
    # Enter your recaptcha secret key here
    secret_key = "secretKey"
    url = "https://www.google.com/recaptcha/api/siteverify"

    # when method is not POST, direct user to login page
    if request.method != "POST":
        return render(request, "login.html")

    # from the frontend, get username, password, and client_key
    username = request.POST.get("username")
    password = request.POST.get("password")
    client_key = request.POST.get("g-recaptcha-response")

    # post recaptcha response to Google's recaptcha api
    response = requests.post(url, data={"secret": secret_key, "response": client_key})
    # if the recaptcha api verified our keys
    if response.json().get("success", False):
        # authenticate the user
        user_in_database = authenticate(request, username=username, password=password)
        if user_in_database:
            login(request, user_in_database)
            return redirect("/your-webpage")
    return render(request, "login.html")
