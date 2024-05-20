function validate() {
    var name = document.getElementById("name").value;
    if (name == ""){
        document.getElementById("name") .style.borderColor = "Red";
    return false;
    }
    var contact = document.getElementById("contact").value;
    var pattern = /^\d{10}$/;
    if(!contact.match(pattern)){
        document.getElementById("errl").innerHTML = "invalid contact no";
        return false;
    }
    var pwd = document.getElementById("pwd").value;
    if(pwd.length < 6){
        document.getElementById("pwderr").innerHTML = "password must be alteast 6";
        return false;
    }
    var cpwd = document.getElementById("cpwd").value;
    if(cpwd != pwd){
        document.getElementById("cpwderr").innerHTML = "password not match";
        return false;
    }

}

 
