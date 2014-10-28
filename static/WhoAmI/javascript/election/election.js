/**
 * Created by garfild on 10/14/14.
 */
//http://stackoverflow.com/questions/23805121/how-to-receive-a-list-in-jquery-from-djangopython

$(document).ready(function () {
    var players = JSON.parse($('#json_players').html());


    $('.vote').mouseenter(function () {
        var end = this.value;
        console.log(end);
        console.log("zakhar");
    });
    $('.ui.dropdown')
        .dropdown()

    ;
    $(".vote").dropdown({
        onChange: function (val) {

//            var index = players.indexOf(val);
//            if (index > -1) {
//                array.splice(index, 1);
//            }
//            dropdownElement = $(".vote");
//            dropdownElement.find('option[value=kazem]').remove();
//            $(".vote option[value=val]").remove();

        }
    })
});

function send_election_form() {
    console.log("Election is sent!");
    $.ajax({
        url:"/game/election_request",
        method:$(this).attr('method'),
        data:$(this).serialize()
    });



}
$(document).ready(function () {
    $('#election_form').submit(function () {
        send_election_form();
    });
});