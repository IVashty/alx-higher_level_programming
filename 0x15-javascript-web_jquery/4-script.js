#!/usr/bin/node
//
import $ from 'jquery';

// function is called when the page has finished loading
$(document).ready(function () {
  const myheader = $('header');
  $('#toggle_header').click(function () {
    if (myheader.hasClass('red')) {
      myheader.removeClass('red');
      myheader.addClass('green');
    } else {
      myheader.removeClass('green');
      myheader.addClass('red');
    }
  });
});
