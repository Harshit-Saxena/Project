function greeting(){
    var name = prompt("What is your name ?");
    var h1 = document.createElement('h1');
    var text = document.createTextNode('Hello '+name);
    h1.setAttribute('id','Name');
    h1.appendChild(text);
    document.getElementById('here').appendChild(text);
}
function reset(){
    document.getElementById('Name').remove(); //this is not working for some rsn 
}