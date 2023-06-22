let radioImg = document.querySelectorAll(".change_img");
let radioButtons = document.querySelectorAll(".change_button");
let divs = document.querySelectorAll(".cool_class");

let loadInp = document.querySelector(".load_file-inp");
let selectGradiant = document.querySelector("#gradiant-select");
let colors = document.querySelector(".colors")

let downloadA = document.querySelector(".download-a")
let createButton = document.querySelector(".create")
let qrImage = document.querySelector("#img-tag")

function unhideInput(){
   loadInp.hidden = false;
}

function hideInput(){
   loadInp.hidden = true;
}

function unhideColors(){
   colors.querySelector("input").hidden = false;
   colors.querySelector("label").hidden = false;
}

function hideColors(){
   colors.querySelector("input").hidden = true;
   colors.querySelector("label").hidden = true;
}

function checkSelectImg(){
   if (selectGradiant.value == "ImageColorMask()"){
      unhideInput()
   }
   else{
      hideInput()
   }
}

function checkSelectCol(){
   if (selectGradiant.value == "SolidFillColorMask()" || selectGradiant.value == "ImageColorMask()" ){
      hideColors()
   }
   else{
      unhideColors()
   }
}

function ghostClick(){
   a =  this.closest("div")
   let butt = a.querySelector(".change_button")
   let imge = a.querySelector(".change_img")
   butt.click()
   radioButtons.forEach((butt2) =>{
      if(butt2 != butt){
         let d = butt2.closest("div")
         let cImge = d.querySelector(".change_img")
         cImge.style = "border: 2px solid #0062FF;"
      }
   }
   )
   imge.style = "border: 2px solid #FF7A33;"
}

radioImg.forEach((button) =>{
   button.addEventListener("click",ghostClick)
}
)

if (qrImage.getAttribute("src") === ""){
   downloadA.hidden = true
}
else{
   downloadA.hidden = false
   createButton.style = "border-radius: 30px 0px 0px 30px; border-right:none"
}

let choose1 = document.querySelector('.first_choose')
choose1.style = "border: 2px solid #FF7A33;"
selectGradiant.addEventListener("change", checkSelectImg)
selectGradiant.addEventListener("change", checkSelectCol)
