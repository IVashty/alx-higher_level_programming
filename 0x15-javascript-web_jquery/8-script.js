// statement to bring in jquery
import $ from 'jquery';
// ensure that the script runs only after the page is fully loaded.
$(document).ready(function () {
  // send a GET request to the provided URL and get the response data
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // a loop in the array
    for (let result = 0; result < data.results.length; result++) {
      $('UL#list_movies').append('<li>' + data.results[result].title + '</li>');
    }
  });
});
