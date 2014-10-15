/**
 * Created by garfild on 9/13/14.
 */

$(document).ready(function () {
//    var url = window.location.pathname;


    var clock = $('.clock').FlipClock(10, {
        clockFace: 'MinuteCounter',
		countdown: true
    });

    var chat_box = $('#message_box');
    var room = $("#room").val();
    var socket = io.connect('http://localhost:8080');

    socket.emit('room', room);
    socket.on('message', function (params) {
        console.log("message is " + params.message);
        var $sender = $('<span></span>').addClass('label label-'+params.sender).text(params.sender);
        $('<p></p>').text(params.message).prepend(': ').prepend($sender).appendTo(chat_box);
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
