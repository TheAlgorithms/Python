"""
Recaptcha is a free captcha service offered by Google
in order to secure websites / forms
https://www.google.com/recaptcha/admin/create (This is the site where
you can get your recaptcha keys created)
* Keep in mind that recaptcha doesn't work with localhost
When you register recaptcha for your site,
you'll get two keys: ClientKey & SecretKey.
ClientKey is to be kept in the front end
SecretKey is to be kept at backend
"""
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
import json
import requests


"""

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
Below one Django function based code for views.py file for a login form
has been shown with recaptcha verification
"""


def login_using_recaptcha(request):
    # when method is not POST, direct user to login page
    if request.method != "POST":
        print('Welcome to LoginPage')
        # return render(request, "login.html")

    # get username, password & client_key from frontend
    username = request.POST.get("username")
    password = request.POST.get("password")
    client_key = request.POST.get("g-recaptcha-response")

    # Keep your recaptcha secret key here
    secret_key = "secretKey"

    # make json of your captcha data
    captcha_data = {"secret": secret_key, "response": client_key}

    # post recaptcha response to Google recaptcha api
    post = requests.post(
        "https://www.google.com/recaptcha/api/siteverify", data=captcha_data
    )
    # read the json response from recaptcha api
    response = json.loads(post.text)
    verify = response['success']
    # if verify is true
    if verify:
        # authenticate user with following code
        # user = authenticate(request, username=username, password=password)
        user = True

        # if user is in database
        if user:
            print('Login success')
            # login user
            # login(request, user)
            # return redirect("/your-webpage")
        else:
            print('invalid crednetial')
            # send user back to the login page again
            # return render(request, "login.html")
    else:
        print('Captcha verification failed')
        # if verify is not true, send user back to login page
        # return render(request, "login.html")
