/**
 * Created by Javad on 9/13/14.
 */

$(document).ready(function() {
    $("#id1").hover(function() {
        $(this).toggleClass("active, visible");
    })
});



$(document).ready(function() {
    $("#player1").click(function() {
        $(this).toggleClass("active, visible");
    })
});

$(document).ready(function() {
    $('.ui.dropdown')
        .dropdown()
    ;
});



/**
 * Created by garfild on 9/13/14.
 */

$(document).ready(function () {
//    var url = window.location.pathname;



    var chat_box = $('#message-box');
    var room = $("#room").val();
    console.log("jeddan chera?");
    console.log(room);
    var socket = io.connect('http://localhost:8080');

    socket.emit('room', room);

    socket.on('message', function (params) {
        console.log("message is " + params.message);
        var $sender = $('<span></span>').addClass('label '+params.sender).text(params.sender);
        $('<p></p>').text(params.message).prepend(': ').prepend($sender).appendTo(chat_box);
    });

//    socket.on('message', function (data) {
//        $("#content").append("<div>" + data.sender + ": " + data.message + "</div>")
//    });s
    //con   sole.log("ajab!");
    $('#message_input').keypress(function (event) {
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
                        $('#message_input').val("");
                        console.log("ajax resid");
                    }
                });
            }
        }
    });
});
