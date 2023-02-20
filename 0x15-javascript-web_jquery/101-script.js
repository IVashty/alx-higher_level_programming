// statement to bring in jquery
import $ from 'jquery';
// ensure that the script runs only after the page is fully loaded.
$(document).ready(function () {
  const mylist = $('UL.my_list');
  // sets an event listener that add new item
  $('DIV#add_item').click(function () {
    mylist.append('<li>Item</li>');
  });

  // sets an event listener that remove last item from ordered list
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  //  sets an event listener that clear list items
  $('DIV#clear_list').click(function () {
    mylist.empty();
  });
});
