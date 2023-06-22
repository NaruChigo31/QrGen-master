let wrapper = document.querySelector(".wrapper-end")
let button = document.querySelector(".end-subscribe")
let modal = document.querySelector(".modal")
let button1 = document.querySelector(".button")

function lightDown(){
    wrapper.style = "opacity: 1; z-index: 4"
    modal.style = "z-index: 6"

}

function lightUp(){
    wrapper.style = "opacity: 0; z-index: -1;"
    modal.style = "z-index: -1"
}

button.addEventListener("click", lightDown)
button1.addEventListener("click", lightUp)
wrapper.addEventListener("click", lightUp)