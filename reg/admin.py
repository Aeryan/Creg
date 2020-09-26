from django.contrib import admin
from .models import Kylastaja


class RegAdmin(admin.ModelAdmin):
    list_display = ('nimi', 'email')


admin.site.register(Kylastaja, RegAdmin)
