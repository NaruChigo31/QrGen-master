let cover = document.querySelector(".modal");
let buttonNo = document.querySelector(".button-no")

function openModal(){
    let cover = document.querySelector(".modal");
    cover.style = "opacity:1; z-index:6;";
}

function closeModal(){
    let cover = document.querySelector(".modal");
    cover.style = "opacity:0; z-index:-1;";
}


buttonNo.addEventListener('click',closeModal);