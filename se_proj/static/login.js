$(function(){
    if(login == "False"){
        document.getElementById("error-box").classList.add("error-box");
        document.getElementById("error-box").innerHTML = "Invalid Credentials";
    }
})