//$ is shorthand for jquery
$(function(){
    const quill = new Quill('#editor', {
        theme: 'snow',
        placeholder: 'Type something here, pal.',
    });

    try {
        text_json = JSON.parse(text);
        quill.setContents(text_json);
    } catch {
        
    }
    
    //getSemanticHTML allows for the easy coversion and display of quill objects
    document.getElementById('display').innerHTML = quill.getSemanticHTML();

    document.getElementById('submit-button').addEventListener('click', function() {
        const data = quill.getContents();
        const stringify_data = JSON.stringify(data)
        $.ajax({
            url: "",
            type: "POST",
            data: {values: stringify_data, csrfmiddlewaretoken: CSRF_TOKEN},
            success: function() {
                quill.deleteText(0, quill.getLength());
            },
        });
    });
});
