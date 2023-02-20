#!/usr/bin/node
//
import $ from 'jquery';

//
$(document).ready(function () {
  const mylist = $('UL.my_list');
  $('DIV#add_item').click(function () {
    mylist.append('<li>Item</li>');
  });
});
