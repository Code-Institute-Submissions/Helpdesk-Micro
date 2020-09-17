// Navbar collapse and add to right of screen on small screens 
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {edge:'right'});
  });



// jQuery
$(document).ready(function(){
    $('.collapsible').collapsible(); /* accordion */
    $('select').formSelect(); /* select dropdowns */
  });