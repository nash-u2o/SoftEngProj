$(function(){
    // Text Initialization

    var quill;
    quill = new Quill('#hidden-editor', {
        theme: 'snow',
        placeholder: 'Type something here, pal.',
    });

    // To use the text in the form Quill stores it in, we have the escape the newline characters for JSON parsing
    escaped_text = text.replace(/\n/g, '\\n');
    try {
        text_json = JSON.parse(escaped_text);
    } catch (error) {
        text_json = "";
    }
    
    quill.setContents(text_json);
    document.getElementById('info').innerHTML = quill.getSemanticHTML();

    // End of Text Initialization

    // Button Initialization

    if(is_teacher == "True"){
        document.getElementsByClassName("edit-button-container")[0].innerHTML = "<button id='edit-button' class='btn btn-success'>Edit</button>";
        document.getElementsByClassName("edit-button-container")[0].classList.add("btn", "btn-success");
    }

    // End of Button Initialization

    // Button Functions 

    // When edit button is clicked, display the Quill editor and put any existing info in it 
    $("#edit-button").on("click", function(){
        // When inserting html using JS, apply classes afterwards
        document.getElementById("info").innerHTML = 
        "<div class='editor-container'>" + 
            "<div id='editor'>" +
            "</div>" +
            "<div id='edit-button-container'>" +
                "<button id='submit-button'>Submit</button>" +
            "</div>" +
        "</div>";
        document.getElementById('submit-button').classList.add('btn', 'btn-success', 'button-styles');
        document.getElementById('submit-button').addEventListener('click', successClick);
        quill = new Quill('#editor', {
            theme: 'snow',
            placeholder: 'Enter Class Information',
        });
        quill.setContents(text_json);
    });

    // When submit is clicked, put the contents in the database
    function successClick (){
        const data = quill.getContents();
        const stringify_data = JSON.stringify(data)

        // Send a post request to the view to store info in database. Causes page to reload
        $.ajax({
            url: "",
            type: "POST",
            data: {values: stringify_data, csrfmiddlewaretoken: CSRF_TOKEN},
            success: function() {
                quill.deleteText(0, quill.getLength());
            },
        });
    };
});
