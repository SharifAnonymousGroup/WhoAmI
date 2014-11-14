/**
 * Created by garfild on 10/14/14.
 */
//http://stackoverflow.com/questions/23805121/how-to-receive-a-list-in-jquery-from-djangopython

$(document).ready(function () {
    var players = JSON.parse($('#json_players').html());


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
        type: 'POST',
        url: "/game/election_request/",
        data: $('#election_form').serialize(),
        success: function (data) {
            console.log("success shod");
            $('.election_message').html(data['message']);
            $('.ui.modal#election_modal')
                .modal('show');
            if(data['is_success']){
//                $('#election_button').prop('disabled', true);
            }


        }
    });


}
$(document).ready(function () {
    $('#election_form').submit(function () {
        send_election_form();
    });
});