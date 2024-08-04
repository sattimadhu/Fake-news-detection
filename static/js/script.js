let send=document.querySelector("#send");
let display=document.querySelector(".display");
let form=document.querySelector(".form");
send.addEventListener('click',function(event){
    event.preventDefault()
    form.submit();
})