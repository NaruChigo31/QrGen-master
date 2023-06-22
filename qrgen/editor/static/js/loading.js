let image = document.querySelector("#img-tag")
let gif = document.querySelector(".gif-load")

function loading(){
        image.style = "display:none"
        gif.style = "display: flex"   
    }

$(document).ready(function(){
    $(".create_form").on("submit", loading);
  });
