from django.apps import AppConfig


class RegConfig(AppConfig):
    name = 'reg'


# Klass lühima aktsepteeritava nimepikkuse hoiustamiseks
class Parameetrid:
    # Seda väärtust kasutavad forms.py ja views.py kaudu templates/reg/reg.html
    lyhimnimi = 7
