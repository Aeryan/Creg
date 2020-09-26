from django import forms
from .apps import Parameetrid


class RegisterForm(forms.Form):

    name_pattern = ".{" + str(Parameetrid.lyhimnimi) + ",50}"

    # Nimevälja deklaratsioon
    nimi = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id': 'nimi',
                                                                        'pattern': name_pattern,
                                                                        'placeholder': "Eesnimi Perekonnanimi"}))

    # E-posti aadressi väli, aktsepteerib HTML5 "email"-tüüpi sisendeid pikkusega [0,50]
    epost = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'id': 'epost',
                                                          'type': "email",
                                                          'pattern': ".{,50}",
                                                          'placeholder': "E-posti aadress"}))
