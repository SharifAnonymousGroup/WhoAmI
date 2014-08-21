/**
 * Created by Iman on 8/19/14.
 */
$(document).ready(function(){
    $('input_box').keypress(function(event){
        var message = $(this).val();
        if($(message != ""){
            $.ajax({
                url: '/chat/send_message',
                method: 'GET',
                data: {
                    message:
                }
            });
        }
    });
});