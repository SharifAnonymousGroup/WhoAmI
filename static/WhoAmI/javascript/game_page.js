/**
 * Created by Javad on 9/13/14.
 */

$(document).ready(function() {
    $("#id1").hover(function() {
        $(this).toggleClass("active, visible");
    })
});



$(document).ready(function() {
    $("#player1").click(function() {
        $(this).toggleClass("active, visible");
    })
});

$(document).ready(function() {
    $('.ui.dropdown')
        .dropdown()
    ;
})