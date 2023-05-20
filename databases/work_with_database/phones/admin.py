from django import forms
from django.contrib import admin
from .models import Phone


class PhoneAdminForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['name', 'price', 'image', 'release_date', 'lte_exists']


class PhoneAdmin(admin.ModelAdmin):
    form = PhoneAdminForm

admin.site.register(Phone, PhoneAdmin)
