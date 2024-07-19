from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission
from exercise.models import Exercises

class ExercisesAjaxDatatableView(AjaxDatatableView):

    model = Exercises
    title = 'Exercises'
    initial_order = [["muscle", "asc"], ]
    length_menu = [[10, 20, 50, 100], [10, 20, 50, 100]]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'muscle', 'visible': True, },
        {'name': 'difficulty', 'visible': True, },
        {'name': 'descriptions', 'visible': True, },
    ]
    #
    # def get_initial_queryset(self, request=None):
    #
    #     user = self.request.user
    #     return self.model.objects.filter(user=user)