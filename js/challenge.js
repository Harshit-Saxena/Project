//Challenge 1: YOB
function box(){
    var birthyear = prompt('In which year were you born....Good friend?');
    if(birthyear === "")
    {
        window.alert("Please enter the birthyear !");
    }
    else if(birthyear>2021){    
        window.alert("Person hasnt been born yet !");
    }
    else {
        var ageIndays = (2021-birthyear)*365;
        var h2=document.createElement('h2');
        var text=document.createTextNode('You are ' + ageIndays + ' days old ');
        h2.setAttribute('id','ageIndays');
        h2.appendChild(text);
        document.getElementById('flex-box-result').appendChild(h2);
    }
}
function erase(){
    let items = document.querySelector('#flexAns').querySelectorAll('h2');
    for(i=0;i<items.length;i++){
        items[i].remove();
    }
}

//Challenge 2: Cat Generator
function generator(){
    var image = document.createElement('img');
    var div = document.getElementById('cat-gen');
    image.src = "https://cdn2.thecatapi.com/images/55f.jpg"
    image.setAttribute('id','cat');
    div.appendChild(image);
}
function reset(){
    let items = document.querySelector('#cat-gen').querySelectorAll('img');
    for(i=0; i < items.length; i++){
        items[i].remove();
    }
}

//Challenge 3: RPS
function rpsgame(yourchoice){
    var humanchoice , botchoice;
    humanchoice = yourchoice.id; //this means the var takes the choice by the id...rock or paper or scissor

    botchoice = numberToChoice(randomRpsInt());
    console.log('Computer chose',botchoice);

    result = decidewinner(humanchoice,botchoice) //[1,0] .. human won | bot lost
    console.log(result);

    message = finalMessage(result);
    console.log(message);

    rpsFrontEnd(yourchoice.id,botchoice,message);
}

function randomRpsInt(){
    return Math.floor(Math.random()*3);
}

function numberToChoice(number){
    return ['rock','paper','scissor'][number];
}

function decidewinner(yourchoice,computerchoice){
    var rpsDataBase =      /*Why did we put '=' here*/
    {
        'rock':{'scissor': 1 ,'rock': 0.5 , 'paper': 0},
        'paper':{'rock': 1 ,'paper': 0.5 , 'scissor': 0},
        'scissor':{'paper': 1 ,'scissor': 0.5 , 'rock': 0},
    };
    var yourScore = rpsDataBase[yourchoice][computerchoice];
    var computerScore = rpsDataBase[computerchoice][yourchoice];

    return [yourScore,computerScore];
}

function finalMessage([yourScore,computerScore]){

    /*const playsound = new Audio('/assets/sounds/cash.mp3');
    playsound.play();*/

    if(yourScore===0){
        return {'message': 'You Lost !','color': 'red'};
    }
    else if(yourScore===0.5){
        return {'message': 'You Tied !','color': 'orange'};
    }
    else{
    return {'message':'You Won !','color':'green'};
    }
}

function rpsFrontEnd(humanImageChoice,computerImageChoice,finalMessage){
    var imageDataBase = {
        'rock': document.getElementById('rock').src,
        'paper': document.getElementById('paper').src,
        'scissor': document.getElementById('scissor').src,
    }

//after human chooses an option all images should be removed

    document.getElementById('rock').remove();
    document.getElementById('paper').remove();
    document.getElementById('scissor').remove();

    var humanDiv = document.createElement('div');
    var botDiv = document.createElement('div');
    var messageDiv = document.createElement('div');

    humanDiv.innerHTML = "<img src='" + imageDataBase[humanImageChoice]+ "' height=150px width =150px style='box-shadow: 0px 10px 50px rgba(37,58,233,1);'>"
    
    messageDiv.innerHTML = "<h1 style='color: " +finalMessage['color'] +"; font-size: 40px; padding: 20px; '>" + finalMessage['message'] + "</h1>" 

    botDiv.innerHTML = "<img src='" + imageDataBase[computerImageChoice]+ "' height=150px width =150px style='box-shadow: 0px 10px 50px rgba(233, 37, 37,1);'>"

    document.getElementById('flex-box-rps').appendChild(humanDiv);
    document.getElementById('flex-box-rps').appendChild(messageDiv);
    document.getElementById('flex-box-rps').appendChild(botDiv);
}

//Challenge 4: Change clr of box
var all_buttons = document.getElementsByTagName('button');
console.log(all_buttons);

var copyAllbuttons = [];
for(i=0; i < all_buttons.length; i++){
    copyAllbuttons.push(all_buttons[i]);
}
console.log(copyAllbuttons);

function buttonClrChange(thing){
    if(thing.value==='red'){
        buttonsRed();
    }
    else if(thing.value==='green'){
        buttonsGreen();
    }
    else if(thing.value==='blue'){
        buttonsBlue();
    }
    else if(thing.value==='reset'){
        buttonsReset();
    }
    else if(thing.value==='random'){
        buttonsRandom();
    }
}

function buttonsRed(){
    for(let i=0; i < all_buttons.length; i++){
        all_buttons[i].classList.remove(all_buttons[i].classList[0]);
        all_buttons[i].classList.add('btn-danger');
    }
}

function buttonsGreen(){
    for(let i=0; i < all_buttons.length; i++){
    all_buttons[i].classList.remove(all_buttons[i].classList[0]);
    all_buttons[i].classList.add('btn-success');
    }
}

function buttonsBlue(){
    for(let i=0; i < all_buttons.length; i++){
    all_buttons[i].classList.remove(all_buttons[i].classList[0]);
    all_buttons[i].classList.add('btn-primary');
    }
}

/*function buttonsReset(){
    for(let i=0; i < all_buttons.length; i++){
    all_buttons[i].classList.remove(all_buttons[i].classList[1]);
    all_buttons[i].classList.add(copyAllbuttons[i]);
    }
} */  //Isnt Running for some rsn

function buttonsRandom(){
    let choices = ['btn-primary','btn-danger','btn-warning','btn-success']

    for(let i=0; i < all_buttons.length; i++){
        let randomNumber = Math.floor( Math.random() * 4 );
        all_buttons[i].classList.remove(all_buttons[i].classList[0]);
        all_buttons[i].classList.add(choices[randomNumber]);
    }
}

//Challenge 5: Black Jack
let blackjackGame = {
    'you': {'scoreSpan': '#your-jack-result','div': '#your-box','score':0},
    'dealer': {'scoreSpan': '#dealer-jack-result','div': '#dealer-box','score':0},
    //'cards' : ['2','3','4','5','6','7','8','9','10','K','J','Q','A'],
};
const YOU = blackjackGame['you'] //Why no semi colon aftr this
const DEALER = blackjackGame['dealer'] //same here

const hitsound = new Audio('/assets/sounds/swish.m4a');

document.querySelector('#btn-hit').addEventListener('click',blackjackhit);
document.querySelector('#btn-deal').addEventListener('click',blackjackDeal);

function blackjackhit(){
    //let card = randomcard();
    showcard();
}

/*function randomcard(){
    let randomIndex = Math.floor( Math.random() * 13 );
    return blackjackGame['card'][randomIndex]
}*/

function showcard(){
    let cardImage = document.createElement('img');
    cardImage.src= 'https://cdn2.bigcommerce.com/n-d57o0b/1kujmu/products/297/images/926/4H__83243.1440113515.480.480.png?c=2';
    document.querySelector(YOU['div']).appendChild(cardImage);
    hitsound.play();
}

function blackjackDeal(){
    let items = document.querySelector('#your-box').querySelectorAll('img');
    for(i=0; i< items.length; i++){
        items[i].remove();
    }
}