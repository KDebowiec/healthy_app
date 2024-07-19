
$(document).ready(function() {
    AjaxDatatableViewUtils.initialize_table(
        $('#datatable_exercises'),
        "{% url 'ajax_datatable_exercises' %}",
        {
            processing: true,
            autoWidth: false,
            full_row_select: true,
            scrollX: false
        }, {},
    );
});