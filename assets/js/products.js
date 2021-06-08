$('#id_collection').on('click', function(event) {
    $("#id_collection_name").val($("#id_collection option:selected").text())
});


$('#clear-images').on('click', function(event) {
    $("#id_main_image").val("")
    $("#id_image").val("")
});
