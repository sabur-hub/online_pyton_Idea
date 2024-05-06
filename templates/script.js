$(document).ready(function() {
    $('#execute-btn').click(function() {
        var code = $('#code-input').val();

        $.post('/execute', {code: code}, function(data) {
            $('#output').text(data.output);
        });
    });
});
