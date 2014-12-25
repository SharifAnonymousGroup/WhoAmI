/**
 * Created by garfild on 9/14/14.
 */

var SITE_URL = 'http://localhost:8000/';
var app = require('express')();
var server = require('http').Server(app);
var url = require('url');
var http = require('http');
app.get('/message', function (request, response) {
    var params = url.parse(request.url, true).query;
    room = params.room;
    io.to(room).emit('message', params);
    response.end();
});


server.listen(3333);

// haji ma az inja Clientim! :)


var io = require('socket.io')(8080);
io.on('connection', function (socket) {
    console.log('someone connected');
    socket.on('room', function (room) {
        socket.join(room);
        io.to(room).emit('event', "ali added");
    });

    socket.on('disconnect', function () {
        console.log('some one disconnected');
    });
});


function validation(socket) {
    //bayad por she :)))
}


app.get('/set_times', function (request, response) {
    console.log('set time umad');
    var params = url.parse(request.url, true).query;
    if (params.turn == 0) {
        io.to(params.room).emit('game_start', params);
        console.log("game start");
    }
    console.log(params.round_duration);
    end_round_time = parseInt(params.round_duration) + parseInt(params.election_duration);
    setTimeout(function () {
        io.to(params.room).emit('election_start', params);
        console.log("election start");
    }); //params.round_duration * 1000);
    setTimeout(function () {
        io.to(params.room).emit('round_start', params);
        console.log("round start");

//        $.ajax({
//            url: SITE_URL + "game/end_round/" ,
//            method:'POST',
//            data:{
//                room : params.room
//            }
//        });
        var post_options = {
            host: "http://localhost",
            port: '8000',
            path: '/game/end_round',
            method: 'GET'
        };
        var post_req = http.request(post_options, function (response) {
            var str = '';
            response.on('data', function (chunk) {
                str += chunk;
            });

            response.on('end', function () {
                console.log(str);
            });
        });
        post_req.write("hello zakhar");
        post_req.end();

    },1);// end_round_time * 1000);


    response.end();
});

app.get('add_user', function () {

});