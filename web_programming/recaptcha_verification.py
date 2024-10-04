"""
Recaptcha, Google tarafından sunulan ücretsiz bir captcha hizmetidir ve web sitelerini
ve formları güvence altına almak için kullanılır. https://www.google.com/recaptcha/admin/create
adresinden yeni recaptcha anahtarları oluşturabilir ve daha önce oluşturduğunuz anahtarları
görebilirsiniz.
* Unutmayın ki recaptcha localhost ile çalışmaz.
Bir recaptcha anahtarı oluşturduğunuzda, iki ayrı anahtar alacaksınız: ClientKey ve SecretKey.
ClientKey sitenizin ön yüzünde tutulmalıdır.
SecretKey sitenizin arka yüzünde tutulmalıdır.

# Aşağıda recaptcha etiketi içeren bir HTML giriş formu örneği gösterilmiştir

    <form action="" method="post">
        <h2 class="text-center">Giriş Yap</h2>
        {% csrf_token %}
        <div class="form-group">
            <input type="text" name="username" required="required">
        </div>
        <div class="form-group">
            <input type="password" name="password" required="required">
        </div>
        <div class="form-group">
            <button type="submit">Giriş Yap</button>
        </div>
        <!-- Aşağıda HTML'nin recaptcha etiketi bulunmaktadır -->
        <div class="g-recaptcha" data-sitekey="ClientKey"></div>
    </form>

    <!-- Aşağıda HTML etiketi içine yerleştirilmesi gereken recaptcha scripti bulunmaktadır -->
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

Aşağıda, recaptcha doğrulamasını göstermek için views.py dosyasında bir giriş formu içeren
bir Django fonksiyonu bulunmaktadır.
"""

import requests

try:
    from django.contrib.auth import authenticate, login
    from django.shortcuts import redirect, render
except ImportError:
    authenticate = login = render = redirect = print


def login_using_recaptcha(request):
    # Recaptcha gizli anahtarınızı buraya girin
    secret_key = "secretKey"  # noqa: S105
    url = "https://www.google.com/recaptcha/api/siteverify"

    # method POST değilse, kullanıcıyı giriş sayfasına yönlendir
    if request.method != "POST":
        return render(request, "login.html")

    # ön yüzden kullanıcı adı, şifre ve client_key al
    username = request.POST.get("username")
    password = request.POST.get("password")
    client_key = request.POST.get("g-recaptcha-response")

    # recaptcha yanıtını Google's recaptcha api'sine gönder
    response = requests.post(
        url, data={"secret": secret_key, "response": client_key}, timeout=10
    )
    # recaptcha api anahtarlarımızı doğruladıysa
    if response.json().get("success", False):
        # kullanıcıyı doğrula
        user_in_database = authenticate(request, username=username, password=password)
        if user_in_database:
            login(request, user_in_database)
            return redirect("/your-webpage")
    return render(request, "login.html")
