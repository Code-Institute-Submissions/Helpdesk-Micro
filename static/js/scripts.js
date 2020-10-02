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
});

$(function() {
    var images = ['bg1.jpg', 'bg2.jpg', 'bg3.jpg'];
    $('body').css({'background': 'url(/static/images/' + images[Math.floor(Math.random() * images.length)] + ')'});
   });
