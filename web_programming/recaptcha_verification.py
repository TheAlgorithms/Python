"""
Recaptcha is a free captcha service offered by Google in order to secure websites / forms
https://www.google.com/recaptcha/admin/create (This is the site where you can get your recaptcha keys created)
* Keep in mind that recaptcha doesn't work with localhost 
When you register recaptcha for your site, you'll get two keys: ClientKey & SecretKey. 
ClientKey is to be kept in the front end
SecretKey is to be kept at backend
"""

"""

# An example HTML login form with recaptcha tag is shown below

    <form action="" method="post">
        <h2 class="text-center">Log in</h2> 
        {% csrf_token %}      
        <div class="form-group">
            <input type="text" name="username" class="form-control" placeholder="Username" required="required">
        </div>
        <div class="form-group">
            <input type="password" name="password" class="form-control" placeholder="Password" required="required">
        </div>
        
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-block">Log in</button>
        </div>
        
        <!-- Below is the recaptcha tag of html -->
        <div class="g-recaptcha" data-sitekey="ClientKey"></div>
      
               
    </form>

    <!-- Below is the recaptcha script to be kept inside html tag -->
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

"""

"""
Below one Django function based code for views.py file for a login form has been shown with recaptcha verification
"""

import json
import requests

def loginUsingRecaptcha(request):

  # When Submit button is clicked
  if request.method == 'POST':
    # get username, password & clientKey from frontend
    username = request.POST.get('username')
    password = request.POST.get('password')
    clientKey = request.POST.get('g-recaptcha-response')

    # Keep your recaptcha secret key here
    secretKey = 'secretKey'

    # make json of your captcha data
    captchaData = {
      'secret': secretKey,
      'response': clientKey
      }
    
    # post recaptcha response to Google recaptcha api
    post = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)

    # read the json response from recaptcha api
    response = json.loads(post.text)
    verify = response['success']

    # if verify is true
    if verify == True:
     #authenticate user
      user = authenticate(request, username = username, password=password)

     # if user is in database
      if user is not None:
        #login user
        login(request, user)
        return redirect('/your-webpage')
      else:
        # else send user back to the login page again
        return render(request, 'login.html')
    else:
      # if verify is not true, send user back to login page
      return render(request, 'login.html')