// 绑定获取验证码事件
function bindCatchBtnClick(){
    // 按照id获取元素

    $("#get_code").on("click",function (event){
        var $this = $(this);
        //获取输入框和框内的值
        var email=$("input[name='email']").val();
        if(!email){
            alert("Please enter the email first!")
            return;
        }
        //通过js发送请求:ajax, 异步的js和xml（json）
        $.ajax({
            // 此处只能用url完全路径，url_for只能用于jinja模板
            url:"/mail",
            method:"POST",
            data:{
                "email":email
            },
            success: function(res){
                var code = res['code'];
                if(code == 200){
                    $this.off('click');
                    // 开始倒计时
                    var countdown = 60;
                    var timer = setInterval(function(){
                        countdown -= 1;
                        if(countdown>0){
                            $this.text(countdown+"seconds later can resend")
                        }else{
                            $this.text("Get code");
                            //重新绑定点击事件
                            bindCatchBtnClick();
                            // 如果不需要倒计时，一定要清除倒计时，否则会一直执行
                            clearInterval(timer);
                        }

                    },1000);
                    alert("Verified code send successfully!");
                }
                else{
                    alert(res['message'])
                }
            }
        })
    });
}

//等网页文档所有元素加载完成后在执行
$(function(){
    bindCatchBtnClick();
});

// $(function (){
//
// });