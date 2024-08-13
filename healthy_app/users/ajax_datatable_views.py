from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission
from nutrition.models import MealPlan
from exercise.models import Exercises
from django.template.loader import render_to_string


class NutritionAjaxDatatableView(AjaxDatatableView):

    model = MealPlan
    title = 'MealPlans'
    # initial_order = [["datetime", "asc"], ]
    length_menu = [[10, 20, 50, 100], [10, 20, 50, 100]]
    search_values_separator = '+'
    meal_plan = MealPlan.meal_json

    column_defs = [
        # AjaxDatatableView.render_row_tools_column_def(),
        # {'name': 'datetime', 'visible': False, },
        {'name': 'general_health', 'visible': True, },
        {'name': 'general_min_kcal', 'visible': True, },
        {'name': 'general_max_kcal', 'visible': True, },
        {'name': 'page_title', 'visible': True, 'searchable': True},
    ]

    def get_initial_queryset(self, request=None):

        user = self.request.user
        return self.model.objects.filter(user=user)

    def render_column(self, row, column, meal_plan=MealPlan.meal_json):
        value = self.column_obj(column).render_column(row)

        if column == 'page_title':
            # return render_to_string('users/show_plans.html', {'object': meal_plan})
            return f'<a href="{'/users/show_plans.html'}">{column}</a>'
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

