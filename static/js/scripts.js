// Navbar collapse and add to right of screen on small screens 
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {edge:'right'});
  });

function getNextSequenceValue(sequenceName){
   var sequenceDocument = mongo.db.counters.findAndModify({
      query:{_id: sequenceName },
      update: {$inc:{sequence_value:1}},
      new:true
   });
   return sequenceDocument.sequence_value;
}

// jQuery
$(document).ready(function(){
    $('.collapsible').collapsible(); /* accordion */
    $('select').formSelect(); /* select dropdowns */
    $('.modal').modal(); /* delete user confirmation */
  });

