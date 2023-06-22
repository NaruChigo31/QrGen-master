let loadInp = document.querySelector(".load_file-inp");
let selectGradiant = document.querySelector("#gradiant-select");
let colors = document.querySelector(".colors")

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
 
 
selectGradiant.addEventListener("change", checkSelectImg)
selectGradiant.addEventListener("change", checkSelectCol)