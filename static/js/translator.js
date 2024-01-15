var lang = 'en'
$('.lang-change').click(function() {
    $('#cover').removeClass('hidden');
    var items = {}
    lang = $(this).attr('lang');
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
});
$('#subscribe-form').submit(function(e) {
    e.preventDefault()
    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('type'),
        data: $(this).serialize(),
        success: function(email) {
            if (lang == 'en') {
                alert("Success subscribed: " + email)
            } else {
                alert(email + " Subscrito")
            }
        }
    })
})