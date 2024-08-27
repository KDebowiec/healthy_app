from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission
from nutrition.models import MealPlan
from exercise.models import Exercises
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import DetailView


class NutritionAjaxDatatableView(AjaxDatatableView):


    model = MealPlan
    title = 'MealPlans'
    length_menu = [[10, 20, 50, 100], [10, 20, 50, 100]]
    search_values_separator = '+'

    column_defs = [
        # AjaxDatatableView.render_row_tools_column_def(),
        # {'name': 'datetime', 'visible': False, },
        {'name': 'general_health', 'visible': True, },
        {'name': 'general_min_kcal', 'visible': True, },
        {'name': 'general_max_kcal', 'visible': True, },
        {'name': 'page_title', 'visible': True, 'searchable': True},
        # {'name': 'meal_json', 'visible': True, 'searchable': False, 'orderable': False},
        {
            'name': 'zobacz_wiecej',
            'visible': True,
            'title': 'Zobacz więcej',
            'searchable': False,
            'orderable': False
        },
    ]

    def get_initial_queryset(self, request=None):

        user = self.request.user
        return self.model.objects.filter(user=user)

    def render_column(self, row, column):

        if column == 'zobacz_wiecej':
            url = reverse('meal_plan_detail', kwargs={'pk': row.pk})
            return f'<a href="{url}">Zobacz więcej</a>'
        return super().render_column(row, column)


class WorkoutsAjaxDatatableView(AjaxDatatableView):

    model = Exercises
    search_values_separator = '+'

    column_defs = [
        {'name': 'muscle', 'visible': True, 'searchable': True},
        {'name': 'difficulty', 'visible': True, },

    ]

    def get_initial_queryset(self, request=None):

        user = self.request.user
        return self.model.objects.filter(user=user)



















































