// key press

$(document).ready(function () {

  $('#btn_translate').click(fetchTranslation);

    $('#language_code').keypress(function(event) {
      if (event.which === 13) {
        fetchTranslation();
      }
    });

    function fetchTranslation() {
      var languCode = $('#language_code').val();

      $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languCode, function(data) {
        var helloTrans = data.hello;
        $('#hello').text(helloTrans);
      });
    }
});
