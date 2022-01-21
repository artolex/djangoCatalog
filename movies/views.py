from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HTML requesti alında django.http altında HttpResponse göndermemiz gerekir.
# http://127.0.0.1:8000 açılınca direk bu sayfa gelmesi için pages appinde urls.py diye dosya oluşturulur
# pages altında oluşturulmuş urls ayarları ana urls.py dosyasında da göstermek gerekir.


def index(request):
    # return HttpResponse('<h1>Hello from pages app</h1>')
    # templates i settingste gösterdik. direk altından pages klasörü altındaki indexi alıyoruz
    return render(request, 'movies/list.html')
    # bu işlemden sonra urls.py altında ayarları yapmak gerekiyor.


def detail(request):
    return render(request, 'movies/detail.html')


def search(request):
    return render(request, 'movies/search.html')
