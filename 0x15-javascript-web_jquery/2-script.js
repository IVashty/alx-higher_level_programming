// statement imports the jQuery library
import $ from 'jquery';
// execute the code when the page Document Object Model (DOM) is ready.
// a click event handler to the selected element,the function inside the curly braces {...} will be executed.
//
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
