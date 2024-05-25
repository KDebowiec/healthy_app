from django import forms


class NutritionGeneralForm(forms.Form):
    # size = forms.IntegerField(label='size', required=True, min_value=1, max_value=7)
    health_choices = [
        ('egg-free', 'bez jaj'), ('fish-free', 'bez ryb'), ('tree-nut-free', 'bez orzechów'),
        ('low-sugar', 'dieta niskocukrowa'), ('vegan', 'dieta wegańska'), ('vegetarian', 'dieta wegetariańska')
    ]
    general_health = forms.MultipleChoiceField(label='general_health', choices=health_choices, widget=forms.CheckboxSelectMultiple)
    general_min_kcal = forms.IntegerField(label='general_min_kcal', required=True)
    general_max_kcal = forms.IntegerField(label='general_max_kcal', required=True)
