from django import forms

from .models import Step


class CreateStepsForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ("week1", "week2", "week3", "week4")

        widgets = {
            "week1": forms.TextInput(attrs={"class": "form-control"}),
            "week2": forms.TextInput(attrs={"class": "form-control"}),
            "week3": forms.TextInput(attrs={"class": "form-control"}),
            "week4": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "week1": "May 10th - May 16th",
            "week2": "May 17th - May 23rd",
            "week3": "May 24th - May 30th",
            "week4": "May 31st - June 6th",
        }


class UpdateStepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ("week1", "week2", "week3", "week4")

        widgets = {
            "week1": forms.TextInput(attrs={"class": "form-control"}),
            "week2": forms.TextInput(attrs={"class": "form-control"}),
            "week3": forms.TextInput(attrs={"class": "form-control"}),
            "week4": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "week1": "May 10th - May 16th",
            "week2": "May 17th - May 23rd",
            "week3": "May 24th - May 30th",
            "week4": "May 31st - June 6th",
        }
