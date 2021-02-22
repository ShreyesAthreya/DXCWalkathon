from django import forms

from .models import Step


class CreateStepsForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ('week1', 'week2', 'week3', 'week4', 'week5')

        widgets = {
            'week1': forms.TextInput(attrs={'class': 'form-control'}),
            'week2': forms.TextInput(attrs={'class': 'form-control'}),
            'week3': forms.TextInput(attrs={'class': 'form-control'}),
            'week4': forms.TextInput(attrs={'class': 'form-control'}),
            'week5': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'week1': 'Feb 15th - Feb 21st',
            'week2': 'Feb 22nd - Feb 28th',
            'week3': 'March 1st - March 7th',
            'week4': 'March 8th - March 14th',
            'week5': 'March 15th - March 17th',
        }


class UpdateStepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ('week1', 'week2', 'week3', 'week4', 'week5')

        widgets = {
            'week1': forms.TextInput(attrs={'class': 'form-control'}),
            'week2': forms.TextInput(attrs={'class': 'form-control'}),
            'week3': forms.TextInput(attrs={'class': 'form-control'}),
            'week4': forms.TextInput(attrs={'class': 'form-control'}),
            'week5': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'week1': 'Feb 15th - Feb 21st',
            'week2': 'Feb 22nd - Feb 28th',
            'week3': 'March 1st - March 7th',
            'week4': 'March 8th - March 14th',
            'week5': 'March 15th - March 17th',
        }
