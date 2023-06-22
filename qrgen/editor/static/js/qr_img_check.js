let downloadA = document.querySelector(".download-a")
let createButton = document.querySelector(".create")
let qrImage = document.querySelector("#img-tag")
let forMobile = document.querySelector(".create-for-mobile")

if (qrImage.getAttribute("src") === ""){
   downloadA.hidden = true
}
else{
   downloadA.hidden = false
   createButton.classList.add("with-media-create")
   // createButton.style = "border-radius: 30px 0px 0px 30px; border-right:none"
}
// if ( createButton.style.width <= 240 )