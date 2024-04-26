/*To do:
* Get text in python
* Pass text through the template
* Throw the text into the div
* Make a teacher and student view using the session. Teacher will have an edit button somewhere
*/

$(function(){
    //See what happens when quill is not assigned anything. Really just needed for getSemanticHtml from delta objects

    //Text Initialization

    var quill;
    quill = new Quill('#hidden-editor', {
        theme: 'snow',
        placeholder: 'Type something here, pal.',
    });

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

    $("#edit-button").on("click", function(){
        //When inserting html in JS, apply styles afterwards
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

    function successClick (){
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
        document.getElementById("info").innerHTML = quill.getSemanticHTML();
        text_json = quill.getContents();
        document.getElementsByClassName("editor-container").innerHTML = 
        "<div class='edit-button-container'>" + 
            "<button id='edit-button'>Edit</button>" + 
        "</div>";
        document.getElementById('edit-button').classList.add('btn', 'btn-success', 'button-styles');
    };
});
