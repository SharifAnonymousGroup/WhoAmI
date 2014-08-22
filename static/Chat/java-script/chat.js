/**
 * Created by Iman on 8/19/14.
 */
$(document).ready(function () {
    $('.chat_input').keypress(function (event) {

        if (event.keyCode == 13) {
            var message = $(this).val();
            if (message != ""){

                send_message(message);
                $(this).val("");
            }

        }

    });
});

send_message = function (message) {
    $.ajax({
        url: '/chat/message_handler',
        method: 'GET',
        data: {
            message: message
        },
        success: function(response) {
            console.log(message);
        }
    });
}