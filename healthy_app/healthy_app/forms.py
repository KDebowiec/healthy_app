from django import forms


class ExerciseForm(forms.Form):
    muscle = forms.CharField(max_length=50)
