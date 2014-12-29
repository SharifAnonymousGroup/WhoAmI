/**
 * Created by garfild on 9/14/14.
 */

var SITE_URL = 'http://localhost:8000/';
var app = require('express')();
var server = require('http').Server(app);
var url = require('url');
var http = require('http');
var django_http = require('http');
var io = require('socket.io')(8080);
function serialize(obj) {
    var str = [];
    for (var p in obj)
        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    return str.join("&");
}
app.get('/message', function (request, response) {
    console.log("agha message reside be node");
    var params = url.parse(request.url, true).query;

    console.log("params.message: " + params.message + " " + params.room + " " + params.sender);
    room = params.room;
    console.log('emit to room: ' + room);
    io.to(room).emit('message', params);
    response.end();
});


server.listen(3333);

// haji ma az inja Clientim! :)


io.on('connection', function (socket) {
    console.log('someone connected');
    socket.emit("send_your_room");
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
    var end_round_time = parseInt(params.round_duration) + parseInt(params.election_duration);
    //console.log(end_round_time);
    io.to(params.room).emit('clean_chat_box', params);
    //console.log("kk " + params.room);
    if (params.turn == 0) {
        io.to(params.room).emit('game_start', params);
        console.log("game start");
    }
    setTimeout(function () {
        io.to(params.room).emit('election_start', params);
        console.log("election start + room: " + params.room);
    }, params.round_duration * 1000);
    setTimeout(function () {
        io.to(params.room).emit('round_start', params);
        console.log("round start");
        console.log(end_round_time);

//        $.ajax({
//            url: SITE_URL + "game/end_round/" ,
//            method:'POST',
//            data:{
//                room : params.room
//            }
//        });
        par = {"room": params.room };
        url2 = 'http://localhost:8000/game/end_round/?' + serialize(par);
        console.log(url2);
        var post_req = django_http.get(url2, function (response) {
            console.log('Start query to django');
            var str = '';
            response.on('data', function (chunk) {
                str += chunk;
            });

            response.on('end', function () {
                console.log("javab az django ooomad");
            });
        });
//        post_req.write("hello zakhar");
        post_req.end();
        
        console.log("before this must be connected");
    }, end_round_time * 1000);

    console.log("fuck your");
    response.end();
});

app.get('add_user', function () {

});