$('document').ready(function () {
  $('input#btn_translate').on('click', function () {
    const lang = $('input#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;

    $.get(url, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
