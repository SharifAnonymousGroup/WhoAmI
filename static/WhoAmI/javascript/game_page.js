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


    //$(document).scrollTop($(document).height());
    var chat_box = $('#message-box');
    chat_box.scrollTop(chat_box.prop('scrollHeight'));
    var room = $("#room").val();
    console.log("jeddan chera?");
    console.log(room);
    var socket = io.connect('http://localhost:8080');

    socket.emit('room', room);

    socket.on('election_start', function(params) {
        changeState('Election of round ' + params.round + 'start');
    });

    socket.on('game_start', function(params) {
        startGame();
    });

    socket.on('round_start', function(params) {
        var prevRound = parseInt(params.round) - 1;
        changeState('Election of round' + prevRound + 'end' + "<br>" + 'Round' + params.round + start);
    });

    socket.on('message', function (params) {
        console.log("message is " + params.message);
        var $sender = $('<span></span>').addClass('label '+params.sender).text(params.sender);
        $('<p></p>').text(params.message).prepend(': ').prepend($sender).appendTo(chat_box);
        chat_box.scrollTop(chat_box.prop('scrollHeight'));
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

    $('#ready-button').click(function(){
        var tmp = this;
        $.ajax({
            url: '/game/ready_for_game/',
            method: 'GET',
            success: function(data) {
                console.log('Ok Im ready');
                tmp.addClass('disabled');
            }
        });
    });

    $('#leave-button').click(function(){
        $.ajax({
            url: '/game/leave_game/',
            method: 'GET',
            success: function(data) {
                window.location = '/game/'
            }
        });
    });
});



/* Now in the end
    Some functions for changing the game state
     For example end round
 */

startGame = function() {
    $('#start-game').modal('show');
};

changeState = function(text) {
    $('#state-text').text(text);
    var tmp = $('#change-state')
        .sidebar({
            overlay: true
        })
        .sidebar('toggle');
    setTimeout(function(){
        tmp.sidebar('toggle');
    }, 3000)
};