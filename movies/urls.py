from django.urls import path
from . import views

# http://127.0.0.1:8000 açılınca direk bu sayfa gelmesi için pages appinde urls.py diye dosya oluşturulur
# pages altında oluşturulmuş urls ayarları ana urls.py dosyasında da göstermek gerekir.

urlpatterns = [
    path('', views.index, name='movies'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
]
# views.py altındaki index ve about fonksiyonlarını çağırır
# path url belirtir. boş ise index about dediğimizde localhost/about olarak çalışır.
