let radioImg = document.querySelectorAll(".form_change_img");
let radioButtons = document.querySelectorAll(".form_change_button");

function ghostClick(){
   a =  this.closest(".cool_class")
   let butt = a.querySelector(".form_change_button")
   let imge = a.querySelector(".form_change_img")
   butt.click()
   radioButtons.forEach((butt2) =>{
      if(butt2 != butt){
         let d = butt2.closest(".cool_class")
         let cImge = d.querySelector(".form_change_img")
         cImge.style = "border: 3px solid #0062FF;"
      }
   }
   )
   imge.style = "border: 3px solid #FF7A33;"
}

radioImg.forEach((button) =>{
   button.addEventListener("click",ghostClick)
}
)

let choose1 = document.querySelector('.first_choose')
choose1.style = "border: 3px solid #FF7A33;"
