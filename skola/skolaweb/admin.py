from django.contrib import admin
from .models import Ucenik, Nastavnik, SkolskaGodina, Razred
# Register your models here.
admin.site.register(Ucenik)
admin.site.register(Nastavnik)
admin.site.register(SkolskaGodina)
admin.site.register(Razred)