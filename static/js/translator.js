$('.lang-change').click(function() {
    $('#cover').removeClass('hidden');
    var items = {}
    var lang = $(this).attr('lang');
    $('.translate').each(function() {
        items[$(this).attr('id')] = $(this).text()
    });
    $.ajax({
        url: `trans/${lang}/`,
        type: "POST",
        data: items,
        success: function(json) {
            $('#cover').addClass('hidden')
            $.each(json, function(k, v) {
                $(`#${k}`).text(v);
            });
        },
        error: function() {
            $('#cover').addClass('hidden');
            alert("No se puso traducir .Revise su conexión");
        }
    })
})