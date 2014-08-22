/**
 * Created by Iman on 8/19/14.
 */
$(document).ready(function () {
    $('.chat_input').keypress(function (event) {

        if (event.keyCode == 13) {
            var message = $(this).val();
            if (message != ""){
                console.log("zakhar");

                send_message(message);
                $(this).val("");
            }

        }

    });
});

send_message = function (message) {
    $.ajax({
        url: '/chat/send_message/',
        method: 'GET',
        data: {
            message: message

        }
    });

}