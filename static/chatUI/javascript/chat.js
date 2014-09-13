/**
 * Created by garfild on 9/13/14.
 */

$(document).ready(function () {
    $('#chat_input').keypress(function (event) {
        if (event.keyCode == 13) {
            var message = $(this).val();
            $.ajax({
                url: 'chat/send_message',
                method: 'GET',
                data: {
                    message: message
                }
            });
        }
    });
});
