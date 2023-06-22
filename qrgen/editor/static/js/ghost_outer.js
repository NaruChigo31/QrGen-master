let outerImg = document.querySelectorAll(".outer-change_img");
let outerButtons = document.querySelectorAll(".outer-change-button");

function outerGhostClick(){
   m =  this.closest(".outer_cool_class")
   let butt = m.querySelector(".outer-change-button")
   let imge = m.querySelector(".outer-change_img")
   butt.click()
   outerButtons.forEach((butt2) =>{
      if(butt2 != butt){
         let d = butt2.closest(".outer_cool_class")
         let cImge = d.querySelector(".outer-change_img")
         cImge.style = "border: 3px solid #0062FF;"
      }
   })
   imge.style = "border: 3px solid #FF7A33;"
}

outerImg.forEach((button2) =>{
    button2.addEventListener("click",outerGhostClick)
})

let outerChoose1 = document.querySelector('.outer_first_choose')
outerChoose1.style = "border: 3px solid #FF7A33;"