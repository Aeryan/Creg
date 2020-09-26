from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .forms import RegisterForm
from .models import Kylastaja
from .apps import Parameetrid


def registratsioon(request):
    # Kui saadetakse POST-meetodil taotlus, on tegemist täidetud ja Javascripti poolt kontrollitud ankeediga.
    # Vastasel juhul on tegemist lehe esmakordse avamisega ning kliendile tuleb saata tühi ankeet.

    if request.method == 'POST':
        # Taotluse sisu salvestamine, töötlemine ja andmebaasi sisestamine
        form = RegisterForm(request.POST)
        if form.is_valid():
            nimi = form.cleaned_data['nimi']
            epost = form.cleaned_data['epost']
            kylastaja = Kylastaja(nimi=nimi, email=epost)
            kylastaja.save()
            # Lehele edukast sooritusest teate lisamine
            messages.success(request, 'Olete peole registreeritud!')
            # Kliendi edusõnumiga ja tühjade väljadega lehele ümber suunamine
            return HttpResponseRedirect('/')

    # Ankeedi ja veebilehe loomine ning viimase tagastamine,
    # kasutades seadistatud nimepikkuse miinimumväärtust
    form = RegisterForm()
    return render(request, 'reg/reg.html', {'form': form,
                                            'nameLen': Parameetrid.lyhimnimi})
