//$ is shorthand for jquery
$(function(){
    const quill = new Quill('#editor', {
        theme: 'snow',
        placeholder: 'Type something here, pal.',
    });

    document.getElementById('submit-button').addEventListener('click', function() {
        const data = JSON.stringify(quill.getContents());
        $.ajax({
            url: "",
            type: "POST",
            data: {values: data, csrfmiddlewaretoken: CSRF_TOKEN},
            success: function() {
                quill.deleteText(0, quill.getLength());
            },
        });
    });
});
