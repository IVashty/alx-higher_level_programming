// statement to bring in jquery
import $ from 'jquery';
// ensure that the script runs only after the page is fully loaded.
$(document).ready(function () {
  // send a GET request to the provided URL and get the response data
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    // updates the text of the HTML tag DIV#hello
    $('#hello').text(data.hello);
  });
});
