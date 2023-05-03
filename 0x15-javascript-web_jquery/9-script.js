$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr',
  function (hello) {
    $('div#hello').text(hello.text);
  });
