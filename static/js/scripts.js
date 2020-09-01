// Navbar collapse and add to right of screen on small screens 
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {edge:'right'});
  });

// jQuery to enable accordion
$(document).ready(function(){
    $('.collapsible').collapsible();
  });