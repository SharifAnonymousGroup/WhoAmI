/**
 * Created by garfild on 9/14/14.
 */

//var NODE_URL = 'localhost:3333/';
var app = require('express')();
var server = require('http').Server(app);
var url = require('url');
app.get('/', function (request, response) {
//    console.log(request.url);
    console.log("someOne Connected");
    var params = url.parse(request.url, true).query;
    room = params.room;
    io.to(room).emit('message',params);
    response.end();



});


server.listen(3333);

// haji ma az inja Clientim! :)


var io = require('socket.io')(8080);
io.on('connection', function (socket) {

    socket.on('room', function (room) {
        socket.join(room);
        io.to(room).emit('event', "ali added");
    });
});

function validation(socket) {
    //bayad por she :)))
}


