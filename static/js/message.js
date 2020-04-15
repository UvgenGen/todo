$( document ).ready(function() {
    console.log( "ready!" );

    $("#message_form").submit(function( event ) {
        event.preventDefault();
        let form = $(this);
        $.ajax({
            type: "POST",
            url: '/messages/',
            data: $(this).serializeArray(),
            headers:{"X-CSRFToken": $('[name="csrfmiddlewaretoken"]').attr('value')},
            success: function (response) {
                $("#todo-list").prepend(
                    '<div class="message" style=' +
                    '"color:' + response.text_color + '; ' +
                    'background-color:' + response.bg_color + ';' + 
                    '">' +
                    response.text +
                    '<button data-id=' + response.id + ' class="delete_message">x</button>' +
                    '</div>'
                );
                form.find("input[type=text], textarea").val("");
            }
        });
      });
      

    $("#todo-list").on('click', '.delete_message', function(){
        let $message = $(this);
        $.ajax({
            type: "DELETE",
            url: '/messages/' + $message.data('id') + '/',
            headers:{"X-CSRFToken": $('[name="csrfmiddlewaretoken"]').attr('value')},
            success: function () {
                $message.parent('.message').remove();
            }
        });
    })
});