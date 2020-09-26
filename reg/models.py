from django.db import models


# Mudel, mis vastab andmebaasis külastajate hoiustamiseks mõeldud tabelile
class Kylastaja(models.Model):
    nimi = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    # Tabeli nime "Kylastaja" mitmuse ümberväärtustamine
    # Vaikimisi lisatakse vajadusel (nt. administraatorilehel) tabeli nimele suffiks "-s",
    # mis pole eestikeelsele sõnale kohane.
    class Meta:
        verbose_name_plural = "Kylastajad"
