/**
 * Created by garfild on 9/13/14.
 */

$(document).ready(function () {
    //console.log("ajab!");
    $('#chat_input').keypress(function (event) {
        if (event.keyCode == 13) {
            console.log("some one enter");
            var message = $(this).val();
            $.ajax({
                url: 'chat/send_message',
                method: 'GET',
                data: {
                    message: message
                }
            });
            $(this).val("");
        }
    });
});
