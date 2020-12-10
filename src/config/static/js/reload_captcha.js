$(document).ready(function() {
    // Добавить кнопку обновления после поля (это можно сделать и в шаблоне)
    // {#$('img.captcha').after(#}
    // {#        $('<a href="#void" class="captcha-refresh">Refresh</a>')#}
    // {#        );#}

    // Обработчик кликов для ссылки обновления
    $('.captcha-refresh').click(function() {
        var $form = $(this).parents('form');
        var url = location.protocol + "//" + window.location.hostname + ":" +
            location.port + "/captcha/refresh/";

        // Сделайте AJAX-вызов
        $.getJSON(url, {}, function(json) {
            $form.find('input[name="captcha_0"]').val(json.key);
            $form.find('img.captcha').attr('src', json.image_url);
        });

        return false;
    });
});