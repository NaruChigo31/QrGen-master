let error = document.querySelector(".error-text")

if (error.innerHTML === " "){
    error.style = "visibility: hidden"
}
else{
    error.style = "visibility: visible; color: white; font-size: 20px; background-color:#c26736; padding: 10px; border-radius: 15px;"
}