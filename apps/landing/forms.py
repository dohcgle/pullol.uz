from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'w-full pl-12 pr-5 py-4 rounded-xl border-2 border-gray-200 focus:border-accent focus:ring-4 focus:ring-accent/20 outline-none transition-all placeholder-gray-400 font-medium',
            'placeholder': 'Ism Sharifingiz (Baxtiyor Mijoz)'
        })
    )
    phone_number = forms.CharField(
        max_length=19,
        min_length=19,
        widget=forms.TextInput(attrs={
            'class': 'w-full pl-12 pr-5 py-4 rounded-xl border-2 border-gray-200 focus:border-accent focus:ring-4 focus:ring-accent/20 outline-none transition-all placeholder-gray-400 font-medium',
            'placeholder': '+998 (__) ___-__-__',
            'id': 'phone_number',
            'maxlength': '19',
            'minlength': '19'
        })
    )

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        return phone.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')

    class Meta:
        model = Application
        fields = ['full_name', 'phone_number', 'region', 'credit_amount', 'collateral']
        widgets = {
            'region': forms.Select(attrs={
                'class': 'w-full pl-12 pr-5 py-4 rounded-xl border-2 border-gray-200 focus:border-accent focus:ring-4 focus:ring-accent/20 outline-none transition-all bg-white font-medium cursor-pointer'
            }),
            'credit_amount': forms.NumberInput(attrs={
                'class': 'hidden', # We will use a visible formatted input and sync to this hidden one
                'id': 'form-credit-amount'
            }),
            'collateral': forms.Select(attrs={
                'class': 'w-full pl-12 pr-5 py-4 rounded-xl border-2 border-gray-200 focus:border-accent focus:ring-4 focus:ring-accent/20 outline-none transition-all bg-white font-medium cursor-pointer'
            }),
        }
