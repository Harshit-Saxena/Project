function changeColor(element){ //For some rsn element is imp here
    var currentColor = element.style.backgroundColor;
    if(currentColor=="red"){
        element.style.backgroundColor ="orange";
    }
    else{
        element.style.backgroundColor ="purple";
    }
    if(currentColor=="purple"){
        element.style.backgroundColor ="red";
    }
}