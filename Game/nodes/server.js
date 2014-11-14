/**
 * Created by garfild on 9/14/14.
 */

var SITE_URL = 'http://localhost:8000/';
var app = require('express')();
var server = require('http').Server(app);
var url = require('url');
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


app.get('set_time/', function (request, response) {
    var params = url.parse(request.url, true).query;
    if(params.turn ==0){
        io.to(params.room).emit('game_start',params);
    }
        setTimeout(function () {
            io.to(params.room).emit('elction_start', params);
        }, params.round_duration);
    setTimeout(function () {
        io.to(params.room).emit('round_start',params);

        $.ajax({
            url: SITE_URL + "game/end_round/" ,
            method:'POST',
            data:{
                room : params.room
            }
        });
    }, params.round_duration + params.election_duration);


    response.end();
});

app.get('add_user',function(){

});