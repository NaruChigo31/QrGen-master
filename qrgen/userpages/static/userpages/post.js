$(document).ready(function(){
    $(".delete").click(function(){
        $.ajax({
            url:$(".url").val(),
            type:"post",
            data:{
                csrfmiddlewaretoken: $("#csrf").val(),
                "delete-pk":$(this).val()
            },
        });
        console.log(this.closest('.qr-div').remove())
    });
});