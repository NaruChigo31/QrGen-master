let button = document.querySelector(".add-eye-button")
let eyeSetsDiv = document.querySelector(".eye-settings")
let input = document.querySelector(".add-eye-input")


function openEye(){
    eyeSetsDiv.style = "display:flex ; height: fit-content"
}

function closeEye(){
    eyeSetsDiv.style = "display: none; height: 0px"    
}

function checkButton(){
    let buttonText = button.innerHTML
    if (buttonText == "Додати"){
        button.innerHTML = "Видалити"
        button.classList.add("delete-eye-button")
        button.classList.remove("add-eye-button")
        input.value = "yes_eye"
        openEye()
    }
    else{
        button.innerHTML = "Додати"
        button.classList.remove("delete-eye-button")
        button.classList.add("add-eye-button")
        input.value = "no_eye"
        closeEye()    
    }
}
closeEye()

button.addEventListener("click", checkButton)