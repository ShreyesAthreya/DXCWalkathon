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
            'week1': 'Enter your steps walked from Jan 4 till Jan 10 in Kilometers',
            'week2': 'Jan 11 till Jan 17 goes here',
            'week3': 'Jan 18 till Jan 24 and so on',
            'week4': 'Jan 25 till Jan 31',
            'week5': 'Feb 1 till Feb 4',
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
            'week1': 'Jan 4 - Jan 10',
            'week2': 'Jan 11 - Jan 17',
            'week3': 'Jan 18 - Jan 24',
            'week4': 'Jan 25 - Jan 31',
            'week5': 'Feb 1 - Feb 4',
        }
