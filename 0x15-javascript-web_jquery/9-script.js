// fetch data

$(document).ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    var helloTrans = data.hello;

    $('#hello').text(helloTrans);
  });
});
