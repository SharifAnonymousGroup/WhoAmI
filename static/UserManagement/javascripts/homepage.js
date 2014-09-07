/**
 * Created by po0ya on 24/08/14.
 */


var demoEntered = 0;
$(document).ready( function() {

    $('#leftside-button').click(function() {

        $('#left-sidebar').sidebar({
            overlay: false,
            exclusive: false

        }).sidebar('toggle');

        $('#right-sidebar').sidebar({
            exclusive: false
        }).sidebar('toggle');

        if (demoEntered == 0 || demoEntered == 3) {
            demoEntered = 2;
            $('#leftside-button').css('marginLeft', '0px').animate(
                {width: "9%"}, 400
            );
            $('#left-sidebar-button-text').css('display', 'none');

            $('#rightside-button').css('marginRight' , '0px' ).animate(
                {width:"9%"},400
            );
            $('#right-sidebar-button-text').css('display','none');

        }
        else {
            demoEntered = 3;
            $('#leftside-button').css('marginLeft', '-10px').animate(
                {width: "16%"}, 400, 'swing', function () {
                    $('#left-sidebar-button-text').css('display', 'inline');
                }
            );
            $('#rightside-button').css('marginRight' , '-10px' ).animate(
                {width:"16%"},400,'swing',function(){
                    $('#right-sidebar-button-text').css('display','inline');}
            );

        }
    });

    $('#rightside-button').click(function(){

        $('#left-sidebar').sidebar({
            overlay: false,
            exclusive: false

        }).sidebar('toggle');

        $('#right-sidebar').sidebar({
            exclusive: false
        }).sidebar('toggle');

        if (demoEntered == 0 || demoEntered == 3) {
            demoEntered = 2;
            $('#leftside-button').css('marginLeft', '0px').animate(
                {width: "9%"}, 400
            );
            $('#left-sidebar-button-text').css('display', 'none');

            $('#rightside-button').css('marginRight' , '0px' ).animate(
                {width:"9%"},400
            );
            $('#right-sidebar-button-text').css('display','none');

        }
        else {
            demoEntered = 3;
            $('#leftside-button').css('marginLeft', '-10px').animate(
                {width: "16%"}, 400, 'swing', function () {
                    $('#left-sidebar-button-text').css('display', 'inline');
                }
            );
            $('#rightside-button').css('marginRight' , '-10px' ).animate(
                {width:"16%"},400,'swing',function(){
                    $('#right-sidebar-button-text').css('display','inline');}
            );

        }
    });

    $('.ui.dropdown').dropdown();
    $('#button-forgotpassword-signin').click(function(){
        $('.ui.modal')
            .modal('show')
    });

});