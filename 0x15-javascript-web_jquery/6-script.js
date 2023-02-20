// imports the jQuery library
import $ from 'jquery';

// ensures that the code runs only after the DOM is fully loaded.
$(document).ready(function () {
  // binds a click event to the DIV#update_header element.
  $('#update_header').click(function () {
    // updates the text content of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
