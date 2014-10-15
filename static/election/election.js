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

            var index = players.indexOf(val);
            if (index > -1) {
                array.splice(index, 1);
            }
        }
    })
});