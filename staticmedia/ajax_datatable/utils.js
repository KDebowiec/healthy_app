
$(document).ready(function() {
console.log('test')
    AjaxDatatableViewUtils.initialize_table(
        $('#datatable_nutrition'),
        "{% url 'ajax_datatable_nutrition' %}",
        {
            processing: true,
            autoWidth: false,
            full_row_select: true,
            scrollX: false
        }, {},
    );
});