from django.db import models

# Create your models here.
class Ucenik(models.Model):
    Ime=models.CharField(max_length=20)
    Prezime=models.CharField(max_length=20)
    DatumRodjenja=models.DateField()
    def __repr__(self):
        return self.Ime+' '+self.Prezime
    
class SkolskaGodina(models.Model):
    Oznaka=models.CharField(max_length=10)
    def __repr__(self):
        return self.Oznaka
    
class Nastavnik(models.Model):
    Ime=models.CharField(max_length=20)
    Prezime=models.CharField(max_length=20)
    def __repr__(self):
        return self.Ime+' '+self.Prezime

class Razred (models.Model):
    Oznaka=models.CharField(max_length=20)
    Razrednik=models.ForeignKey(Nastavnik, on_delete=models.CASCADE)
    SkolskaGodina=models.ForeignKey(SkolskaGodina, on_delete=models.CASCADE)
    Ucenici=models.ManyToManyField(Ucenik)
    def __repr__(self):
        return '{} ({} {})'.format(self.Oznaka, self.Razrednik.Ime, self.Razrednik.Prezime)