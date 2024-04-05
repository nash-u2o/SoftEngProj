/*To do:
* Get text in python
* Pass text through the template
* Throw the text into the div
* Make a teacher and student view using the session. Teacher will have an edit button somewhere
*/

$(function(){
    //See what happens when quill is not assigned anything. Really just needed for getSemanticHtml from delta objects
    const quill = new Quill('#editor', {
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

});
