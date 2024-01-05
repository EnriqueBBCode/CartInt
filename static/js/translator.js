$('.lang-change').click(function() {
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
            $.each(json, function(k, v) {
                alert(k + v);
                $(`#${k}`).text(v);
            });
        }
    })
})