/**
 * Created by po0ya on 24/08/14.
 */


//the link: http://stackoverflow.com/questions/7335780/how-to-post-a-django-form-with-ajax-jquery
//link:http://stackoverflow.com/questions/20306981/how-do-i-integrate-ajax-with-django-applications
//link:http://stackoverflow.com/questions/10894484/get-key-value-of-dictionary-by-index-in-jquery
//link:http://stackoverflow.com/questions/17768105/jquery-json-decode-php-to-javascript
//link:http://stackoverflow.com/questions/1208067/wheres-my-json-data-in-my-incoming-django-request
//link:http://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python
function prepare_form(form_id, message_place) {
    $(form_id).submit(function () {
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function (response) {
//console.log($(this).attr('action'));//chera kar nemikone?ba'd bala kar mikone??



//link:http://stackoverflow.com/questions/1189468/jquery-selecting-and-filtering-elements-inside-a-div
//http://stackoverflow.com/questions/306583/this-selector-and-children
                $('.message_holder').html("");
                if(response["is_successful"] == false){
                    var error = response["message"];
                    for (var key in error) {
                        $(message_place).append("<p style='color:red'>" + key + ":</br>&nbsp&nbsp" + error[key] + "</br>" + "</p>");
                    }
                }
                else{
                    var message = response['message'];
                    if(form_id==='#form-signup' || form_id==='#form-forgot'){
                        $(message_place).append("<p style='color:green'>" + message + "</p>");
                    }
                    else{
                        window.location = "/game/";
                    }
                }
//              var myArray = JSON.parse(response);//in chist?
            }
        });
    });

};

var demoEntered = 0;
$(document).ready(function () {

    $('#leftside-button').click(function () {

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
                {width: "5%"}, 400
            );
            $('#left-sidebar-button-text').css('display', 'none');

            $('#rightside-button').css('marginRight', '0px').animate(
                {width: "5%"}, 400
            );
            $('#right-sidebar-button-text').css('display', 'none');

        }
        else {
            demoEntered = 3;
            $('#leftside-button').css('marginLeft', '-1%').animate(
                {width: "12%"}, 400, 'swing', function () {
                    $('#left-sidebar-button-text').css('display', 'inline');
                }
            );
            $('#rightside-button').css('marginRight', '-1%').animate(
                {width: "12%"}, 400, 'swing', function () {
                    $('#right-sidebar-button-text').css('display', 'inline');
                }
            );

        }
    });

    $('#rightside-button').click(function () {

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
                {width: "5%"}, 400
            );
            $('#left-sidebar-button-text').css('display', 'none');

            $('#rightside-button').css('marginRight', '0px').animate(
                {width: "5%"}, 400
            );
            $('#right-sidebar-button-text').css('display', 'none');

        }
        else {
            demoEntered = 3;
            $('#leftside-button').css('marginLeft', '-1%').animate(
                {width: "12%"}, 400, 'swing', function () {
                    $('#left-sidebar-button-text').css('display', 'inline');
                }
            );
            $('#rightside-button').css('marginRight', '-1%').animate(
                {width: "12%"}, 400, 'swing', function () {
                    $('#right-sidebar-button-text').css('display', 'inline');
                }
            );

        }
    });

    $('.ui.dropdown').dropdown();
    $('#button-forgotpassword-signin').click(function () {
        $('.ui.modal')
            .modal('show')
        $('.message_holder').html("");
    });

    prepare_form('#form-signup','.signup_message_holder');
    prepare_form('#form-signin','.signin_message_holder');
    prepare_form('#form-forgot','.signin_message_holder');



});

