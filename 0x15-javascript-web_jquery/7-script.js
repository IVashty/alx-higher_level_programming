// statement imports the jQuery library
import $ from 'jquery';
// ensure that the script runs only after the page is fully loaded.
$(document).ready(function () {
  // make an AJAX request using
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // retrieve character data
    $('#character').text(data.name);
  });
});
