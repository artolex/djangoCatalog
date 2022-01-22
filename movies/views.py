from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Movie

# aynı dizinde olduğu için . models yazıyoruz


# HTML requesti alında django.http altında HttpResponse göndermemiz gerekir.
# http://127.0.0.1:8000 açılınca direk bu sayfa gelmesi için pages appinde urls.py diye dosya oluşturulur
# pages altında oluşturulmuş urls ayarları ana urls.py dosyasında da göstermek gerekir.


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }

    # return HttpResponse('<h1>Hello from pages app</h1>')
    # templates i settingste gösterdik. direk altından pages klasörü altındaki indexi alıyoruz
    return render(request, 'movies/list.html',context) # html sayfaya contexti gönderip {{ key }} şeklinde alabiliriz.
    # bu işlemden sonra urls.py altında ayarları yapmak gerekiyor.


def detail(request, movie_id):
    # Aşağıdaki kod eğer movie objesi bulunamazsa 404 hatası çıkarır. .get(pk = movie_id) pk = primary key
    # try:
    #     movie = Movie.objects.get(pk = movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404("Aradığınız kayıt yok")

    # Yukardaki kod yerine get_object_or_404 fonksiyonunu kullanarak tek satırla yapabiliriz.

    movie = get_object_or_404(Movie, pk = movie_id) # Obje hangi classtan alınıcak, ve PK ne olucak bilgisini veririz
    context = {
        'movie':movie
    }
    return render(request, 'movies/detail.html',context)


def search(request):
    return render(request, 'movies/search.html')
