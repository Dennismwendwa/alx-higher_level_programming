// update the DOM

$(document).ready(function() {
  // adding new element
  $('#add_item').click(function() {
    
    var newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  // remove item
  $('#remove_item').click(function() {
    var list = $('ul.my_list');
    list.children('li:last').remove();
  });

  // clear all items
  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
