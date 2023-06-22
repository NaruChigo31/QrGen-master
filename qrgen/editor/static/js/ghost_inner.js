let innerImg = document.querySelectorAll(".inner-change_img");
let innerButtons = document.querySelectorAll(".inner-change-button");

function innerGhostClick(){
   n =  this.closest(".inner_cool_class")
   let butt = n.querySelector(".inner-change-button")
   let imge = n.querySelector(".inner-change_img")
   butt.click()
   innerButtons.forEach((butt2) =>{
      if(butt2 != butt){
         // console.log(butt2)
         let d = butt2.closest(".inner_cool_class")
         let cImge = d.querySelector(".inner-change_img")
         cImge.style = "border: 3px solid #0062FF;"
      }
   })
   imge.style = "border: 3px solid #FF7A33;"
}

innerImg.forEach((button1) =>{
   button1.addEventListener("click",innerGhostClick)
})

let innerChoose1 = document.querySelector('.inner_first_choose')
innerChoose1.style = "border: 3px solid #FF7A33;"