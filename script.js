function sendMessage(){

let message = document.getElementById("message").value;

fetch("/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:message})
})
.then(res=>res.json())
.then(data=>{
document.getElementById("response").innerText=data.reply;
})

}