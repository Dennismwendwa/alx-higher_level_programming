// say hello

$(document).ready(function() {
  $('#btn_translate').click(function() {
    var languCode = $('INPUT#language_code').val();
    console.log(languCode)

    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languCode, function(data, textStatus) {
      
      var helloTrans = data.hello;

      $('#hello').text(helloTrans);
    });
  });
});
