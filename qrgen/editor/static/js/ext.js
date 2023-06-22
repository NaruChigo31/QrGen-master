let extensionAll = document.querySelectorAll(".extension-div")
let radioAll = document.querySelectorAll(".radio-ext")

let choose2 = document.querySelector('.first_choose_ext')
choose2.style = "background: #c45417;"

function ghostClick2(){
    a =  this
    let butt = a.querySelector(".radio-ext")
    let d = butt.closest(".extension-div")
    butt.click()
    radioAll.forEach((butt2) =>{
       if(butt2 != butt){
          let d = butt2.closest(".extension-div")
          d.style = "background: none"
       }
    }
    )
    d.style = "background: #c45417;"
 }
 
extensionAll.forEach((extButton) =>{
    extButton.addEventListener("click",ghostClick2)
})