// importing the jQuery library so that we can assign the $ var to it
import $ from 'jquery';

// function is called when the page has finished loading
// a click event listener to it using the click() method.
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
