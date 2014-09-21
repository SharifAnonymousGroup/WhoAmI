/**
 * Created by garfild on 9/13/14.
 */

$(document).ready(function () {
//    var url = window.location.pathname;
    var chat_box = $('#message_box');
    var room = $("#room").val();
    var socket = io.connect('http://localhost:8080');

    socket.emit('room', room);
    socket.on('message', function (params) {
        console.log(params.sender);
        chat_box.append('<p>'+params.message+ '</p>');
    });

//    socket.on('message', function (data) {
//        $("#content").append("<div>" + data.sender + ": " + data.message + "</div>")
//    });
    //con   sole.log("ajab!");
    $('#chat_input').keypress(function (event) {
        if (event.keyCode == 13) {
            console.log("some one enter");
            var message = $(this).val();
            if (message != '') {
                $.ajax({
                    url: '/game/chat/send_message',
                    method: 'GET',
                    data: {
                        message: message
                    }
                });
            };
            $(this).val("");
        }
    });
});
