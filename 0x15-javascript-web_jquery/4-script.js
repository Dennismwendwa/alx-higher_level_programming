// toggle between classes

$(document).ready(function() {
  $('#toggle_header').click(function() {
    var headerElem = $('header');

    if (headerElem.hasClass('red')) {
      headerElem.removeClass('red').addClass('green');
    } else {
      headerElem.removeClass('green').addClass('red');
    }
  });
});
