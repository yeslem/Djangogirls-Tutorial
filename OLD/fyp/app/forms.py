from django import forms
from app.models import *


class AppForm(forms.Form):
    # PRESSURE_CHOICES = (('1', 'Internal Pressure'), ('2', 'External Pressure'))
    MATRIAL_CHOISES = ((235000, 'Material 1'), (260000, 'Material 2'), (310000, 'Material 3'), (0, 'Other'))

    # pressure_select = forms.ChoiceField(choices = PRESSURE_CHOICES, required=True)
    materials_select = forms.ChoiceField(choices = MATRIAL_CHOISES, required=True)


    pressure_input = forms.CharField(required=True,
        max_length=64,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Pressure',
            'autofocus': '',
            'id': 'pressure_input'}
        ),
    )

    internal_radius_input = forms.CharField(required=True,
        max_length=64,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Internal Radius',
            'autofocus': ''}
        ),
    )

    joint_efficiency_input = forms.CharField(required=True,
        max_length=64,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Joint Efficiency',
            'autofocus': ''}
        ),
    )

    # Volume_input = forms.CharField(
    #     max_length=64,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Volume',
    #         'autofocus': ''}
    #     ),
    # )

    tan2tan_input = forms.CharField(required=False,
        max_length=64,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tagent to tangent Length',
            'autofocus': ''}
        ),
    )


    corr_allow_input = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'corrosion allowance',
            'autofocus': ''}
        ),
    )

    allow_stress_input = forms.CharField(required=False,
        max_length=64,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Material allowable stress',
            'autofocus': ''}
        ),
    )


    def clean_pressure_select(self):
        return self.cleaned_data.get('pressure_select')

    def clean_materials_select(self):
        return self.cleaned_data.get('materials_select')

    def clean_pressure_input(self):
        return self.cleaned_data.get('pressure_input')

    def clean_internal_radius_input(self):
        return self.cleaned_data.get('internal_radius_input')

    def clean_joint_efficiency_input(self):
        return self.cleaned_data.get('joint_efficiency_input')

    def clean_tan2tan_input(self):
        return self.cleaned_data.get('tan2tan_input')

    def clean_corr_allow_input(self):
        return self.cleaned_data.get('corr_allow_input')

    def clean_allow_stress_input(self):
        return self.cleaned_data.get('allow_stress_input')

    


    # def what_type(self):
    #     if True:
    #         return True
    #     else:
    #         return False
