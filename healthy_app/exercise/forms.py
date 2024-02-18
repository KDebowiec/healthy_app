from django import forms



class ExerciseForm(forms.Form):
    email = forms.EmailField(label='Email')
    muscle = forms.CharField(max_length=50)
    difficulty = forms.ChoiceField(widget=forms.RadioSelect, choices=[('beginner', 'Łatwe'), ('intermediate', 'Średnie'), ('advanced', 'Zaawansowane')])
