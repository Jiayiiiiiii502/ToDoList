
var completed=document.getElementById("completed");

completed.onclick=function(){
    alert("U click the completed bottom")
        const status = true;
        $.ajax({
            url:"/list/home",
            type:"GET",
            data: status,
            success:function(){
                alert("U change the status")
            },
        });
    }



