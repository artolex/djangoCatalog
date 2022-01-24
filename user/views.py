from copyreg import constructor
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # kullanıcı login olduktan sonra session oluşturmak ve kullanıcıya atamak gerekiyor.
            auth.login(request, user)
            # print('login başarılı')
            messages.add_message(request, messages.SUCCESS, "Oturum Açıldı")
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "Hatalı işlem")
            return redirect('login')

    else:
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':  # Sayfada formda submite tıklanıp POST gönderildiğinde
        # dönen bilgiyi database ekayıt etmek için kullan

        # get user values
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(
                    request, messages.WARNING, "Bu kullanıcı adı daha önce alınmış")
                # print("Bu kullanıcı adı daha önce alınmış")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    # print("Bu email daha önce alınmış")
                    messages.add_message(
                        request, messages.WARNING, "Bu email daha önce alınmış")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,
                                                    password=password, email=email)
                    user.save()
                    messages.add_message(
                        request, messages.SUCCESS, "kullanıcı oluşturuldu")

                    # print("kullanıcı oluşturuldu")
                    return redirect('login')
        else:
            # print("Parolalar eşleşmiyor")
            messages.add_message(
                request, messages.WARNING, "Parolalar Eşleşmiyor.")
            return redirect('register')

    else:
        return render(request, 'user/register.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.add_message(
            request, messages.SUCCESS, "Çıkış Yapıldı")
        return redirect('index')
