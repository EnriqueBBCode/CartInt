$('.lang-change').click(function() {
    $('#cover').removeClass('hidden');
    var items = {}
    var lang = $(this).attr('lang');
    $('.translate').each(function() {
        items[$(this).attr('id')] = $(this).text()
        if ($(this).hasClass('placeholder-translate')) {
            items[$(this).attr('id')] = $(this).attr('placeholder')
        }
    });
    $.ajax({
        url: `trans/${lang}/`,
        type: "POST",
        data: items,
        success: function(json) {
            $('#cover').addClass('hidden')
            $.each(json, function(k, v) {
                if ($(`#${k}`).hasClass('placeholder-translate')) {
                    $(`#${k}`).attr('placeholder', v);
                } else { $(`#${k}`).text(v); }
            });
        },
        error: function() {
            $('#cover').addClass('hidden');
            alert("No se puso traducir .Revise su conexión");
        }
    })
})