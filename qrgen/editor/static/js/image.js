let image = document.querySelector("#img-tag")

if (image.getAttribute("src") === ""){
    console.log(1)
    image.setAttribute("src", "{% static 'editor/image/rickroll.jpg' %}")
}