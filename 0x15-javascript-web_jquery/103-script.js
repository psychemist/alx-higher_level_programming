$(document).ready(function () {
  $('input#btn_translate').on('click', function () {
    translate();
  });
  $('input#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});

function translate () {
  const lang = $('input#language_code').val();
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;

  $.get(url, function (data) {
    $('div#hello').text(data.hello);
  });
}
