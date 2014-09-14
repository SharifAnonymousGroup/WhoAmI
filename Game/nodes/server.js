/**
 * Created by garfild on 9/14/14.
 */

//var NODE_URL = 'localhost:3333/';
var app = require('express')();
var server = require('http').Server(app);
app.use('/', function (request, response) {
    console.log("someOne Connected");
});


server.listen(3333);

// haji ma az inja Clientim! :)



var io = require('socket.io')();

io.on('connection', function (socket) {
    console.log("a user connected");
});