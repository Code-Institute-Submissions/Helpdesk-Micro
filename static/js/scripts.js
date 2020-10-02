// Navbar collapse and add to right of screen on small screens
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".sidenav");
  var instances = M.Sidenav.init(elems, { edge: "right" });
});

// jQuery
$(document).ready(function () {
  $(".collapsible").collapsible(); /* accordion */
  $("select").formSelect(); /* select dropdowns */
  $(".modal").modal(); /* delete user confirmation */
  $(".collapsible-header:contains('High')").addClass('red'); /* adds class to collapsible header */
  $(".collapsible-header:contains('Medium')").addClass('blue');
  $(".collapsible-header:contains('Low')").addClass('green');
  $(".collapsible-header:contains('Information')").addClass('yellow');
});



// random background image on page refresh
$(function() {
    var images = ['bg1.jpg', 'bg2.jpg', 'bg3.jpg', 'bg4.jpg'];
    $('.bg-img').css({'background': 'url(/static/images/' + images[Math.floor(Math.random() * images.length)] + ')'});
   });
