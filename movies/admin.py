from django.contrib import admin

from .models import Movie
# Oluşturduğumuz modeli yukarda import edip aşağıda register ediyoruz.


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date", "isPublished")
    list_display_links = ("id", "name")  # name link olmaları için
    list_filter = ("created_date",)  # gün ay vb için filtre ekler.
    # Vizyonda mı diye buton ekler ve değiştirilebilir.
    list_editable = ("isPublished",)
    search_fields = ("name", "description")  # arama fieldı ekler
    list_per_page = 20  # 20 kayıtta yeni sayfa açar.

# admin panelinde gösterimi özelleştirmek için. Modelimizdeki fieldları kullanabiliriz.


admin.site.register(Movie, MovieAdmin)
