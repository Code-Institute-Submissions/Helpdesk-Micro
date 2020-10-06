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
  $(".collapsible-header:contains('High')").addClass('priority-high'); /* adds class to collapsible header */
  $(".collapsible-header:contains('Med')").addClass('priority-med');
  $(".collapsible-header:contains('Low')").addClass('priority-low');
  $(".collapsible-header:contains('Info')").addClass('priority-info');
});



// random background image on page refresh
$(function() {
    var images = ['bg1.jpg', 'bg2.jpg', 'bg3.jpg', 'bg4.jpg'];
    $('.bg-img').css({'background': 'url(/static/images/' + images[Math.floor(Math.random() * images.length)] + ')'});
   });
