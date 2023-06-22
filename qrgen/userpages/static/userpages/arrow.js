

window.addEventListener('scroll',(event)=>{
    let arrowTop = document.querySelector('#arrowTop');
    let arrowDown = document.querySelector('#arrowDown');
    if (window.scrollY<document.body.scrollHeight/4){
        add(arrowDown);
        arrowDown.style = 'opacity:1;';
        // opacity:1;
        arrowTop.style = 'opacity:0;'
        // opacity:0;
        setTimeout(5000,remove(arrowTop));
    }
    if (window.scrollY>document.body.scrollHeight/4){
        add(arrowTop)
        arrowTop.style = 'opacity:1;';
        arrowDown.style = 'opacity:0;'
        setTimeout(5000,remove(arrowDown));
    }
}
)
arrowTop.addEventListener('click',(event)=>{
    setTimeout(200,window.scrollTo(0,0))
})
arrowDown.addEventListener('click',(event)=>{
    setTimeout(200,window.scrollTo(0,document.body.scrollHeight))
})

function remove(arrow){
    arrow.style = "display:none;"
}

function add(arrow){
    arrow.style = "display:block;"
}