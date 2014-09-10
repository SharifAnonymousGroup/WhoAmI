/**
 * Created by po0ya on 24/08/14.
 */


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
                {width: "9%"}, 400
            );
            $('#left-sidebar-button-text').css('display', 'none');

            $('#rightside-button').css('marginRight', '0px').animate(
                {width: "9%"}, 400
            );
            $('#right-sidebar-button-text').css('display', 'none');

        }
        else {
            demoEntered = 3;
            $('#leftside-button').css('marginLeft', '-10px').animate(
                {width: "16%"}, 400, 'swing', function () {
                    $('#left-sidebar-button-text').css('display', 'inline');
                }
            );
            $('#rightside-button').css('marginRight', '-10px').animate(
                {width: "16%"}, 400, 'swing', function () {
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
                {width: "9%"}, 400
            );
            $('#left-sidebar-button-text').css('display', 'none');

            $('#rightside-button').css('marginRight', '0px').animate(
                {width: "9%"}, 400
            );
            $('#right-sidebar-button-text').css('display', 'none');

        }
        else {
            demoEntered = 3;
            $('#leftside-button').css('marginLeft', '-10px').animate(
                {width: "16%"}, 400, 'swing', function () {
                    $('#left-sidebar-button-text').css('display', 'inline');
                }
            );
            $('#rightside-button').css('marginRight', '-10px').animate(
                {width: "16%"}, 400, 'swing', function () {
                    $('#right-sidebar-button-text').css('display', 'inline');
                }
            );

        }
    });

    $('.ui.dropdown').dropdown();
    $('#button-forgotpassword-signin').click(function () {
        $('.ui.modal')
            .modal('show')
    });
    /*
     $('.ui.form')
     .form({
     firstName: {
     identifier: 'first_name',
     rules: [
     {
     type: 'empty',
     prompt: 'Please enter your first name'
     }
     ]
     },
     lastName: {
     identifier: 'last_name',
     rules: [
     {
     type: 'empty',
     prompt: 'Please enter your last name'
     }
     ]
     },
     email: {
     identifier: 'email',
     rules: [
     {
     type: 'email',
     prompt: 'Please enter correct email address'
     }
     ]
     },
     username: {
     identifier: 'username',
     rules: [
     {
     type: 'empty',
     prompt: 'Please enter a username'
     }
     ]
     },
     age: {
     identifier: 'age',
     rules: [
     {
     type: 'empty',
     prompt: 'Please enter your age'
     }
     ]
     },

     password: {
     identifier: 'password',
     rules: [
     {
     type: 'empty',
     prompt: 'Please enter a password'
     },
     {
     type: 'length[6]',
     prompt: 'Your password must be at least 6 characters'
     }
     ]
     },
     confirm_password: {
     identifier: 'confirm_password',
     rules: [
     {
     type: 'empty',
     prompt: 'Please enter your password again'
     },
     {
     type: 'match[password]',
     prompt: 'Your password does not match with above password'

     }
     ]
     },
     terms: {
     identifier: 'terms',
     rules: [
     {
     type: 'checked',
     prompt: 'You must agree to the terms and conditions'
     }
     ]
     }
     }, {
     on: 'blur',
     inline: 'true'
     });

     */
});
//the link: http://stackoverflow.com/questions/7335780/how-to-post-a-django-form-with-ajax-jquery
//link:http://stackoverflow.com/questions/20306981/how-do-i-integrate-ajax-with-django-applications
//link:http://stackoverflow.com/questions/10894484/get-key-value-of-dictionary-by-index-in-jquery
//link:http://stackoverflow.com/questions/17768105/jquery-json-decode-php-to-javascript
//link:http://stackoverflow.com/questions/1208067/wheres-my-json-data-in-my-incoming-django-request
//link:http://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python
function send_form(form_id,message_place) {
    console.log("WHAT IS YOUR NAME");
    $(form_id).submit(function () {
        console.log("dafaat");
        $.ajax({

            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function (response) {
//                console.log($(this).attr('action'));//chera kar nemikone?ba'd bala kar mikone??


                console.log("ajax is inja");
//link:http://stackoverflow.com/questions/1189468/jquery-selecting-and-filtering-elements-inside-a-div
//http://stackoverflow.com/questions/306583/this-selector-and-children
                $('.message_holder').html("");
//                var myArray = JSON.parse(response);//in chist?
                var error = response["err"];
                for(var key in error){
                    $(message_place).append("<p style='color:red'>"+key+":</br>&nbsp&nbsp"+error[key]+"</br>"+"</p>");

                }

            }


        });
    });

};
