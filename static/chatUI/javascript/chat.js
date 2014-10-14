/**
 * Created by garfild on 9/13/14.
 */

$(document).ready(function () {
//    var url = window.location.pathname;
    var data = $(window.start_time);
    console.log("start time is " + data);
    var clock = $('.clock').FlipClock(10, {
        clockFace: 'MinuteCounter',
		countdown: true
    });

    var chat_box = $('#message_box');
    var room = $("#room").val();
    var socket = io.connect('http://localhost:8080');

    socket.emit('room', room);
    socket.on('message', function (params) {
        chat_box.append('<p>'+params.sender+": " + params.message+ '</p>');
    });

//    socket.on('message', function (data) {
//        $("#content").append("<div>" + data.sender + ": " + data.message + "</div>")
//    });s
    //con   sole.log("ajab!");
    $('#chat_input').keypress(function (event) {
        if (event.keyCode == 13) {
            //console.log("some one enter");
            var message = $(this).val();
            if (message != '') {
                $.ajax({
                    url: '/game/chat/send_message/',
                    method: 'GET',
                    data: {
                        message: message
                    },
                    success: function(data) {
                        $('#chat_input').val("");
                        console.log("ajax resid");
                    }
                });
            }
        }
    });
});
