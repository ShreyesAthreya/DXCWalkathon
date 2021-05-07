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
            "week1": "May 10th - May 17st",
            "week2": "May 18th - May 24th",
            "week3": "May 25st - May 31st",
            "week4": "June 1th - June 7th",
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
            "week1": "May 10th - May 17st",
            "week2": "May 18th - May 24th",
            "week3": "May 25st - May 31st",
            "week4": "June 1th - June 7th",
        }
