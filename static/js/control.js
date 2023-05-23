// 监听判断手机号格式
function phone_listen(){
    var reg_phone = /^1[3-9][0-9]{9}$/;
    var phone = document.getElementById('phone').value;
    var reg_email = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    var email = document.getElementById('email').value;

    if(reg_phone.test(phone)){
        document.getElementById('phone_alter').innerHTML = '';
        if (reg_email.test(email)){
            document.getElementById("btn_send_contact").removeAttribute("disabled");
            document.getElementById("btn_send_contact").style.backgroundColor  = 'black';
        }
    }else {
        document.getElementById('phone_alter').innerHTML = '手机号格式错误';
        document.getElementById("btn_send_contact").setAttribute("disabled", true);
        document.getElementById("btn_send_contact").style.backgroundColor  = '#555555';

    }
}
 // 监听判断邮箱格式
function email_listen(){
    var reg_phone = /^1[3-9][0-9]{9}$/;
    var phone = document.getElementById('phone').value;
    var reg_email = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    var email = document.getElementById('email').value;
    if (reg_email.test(email)){
        document.getElementById('email_alter').innerHTML = '';
        if(reg_phone.test(phone)){
            document.getElementById("btn_send_contact").removeAttribute("disabled");
            document.getElementById("btn_send_contact").style.backgroundColor  = 'black';
        }

    }else{
        document.getElementById('email_alter').innerHTML = '邮箱格式错误';
        document.getElementById("btn_send_contact").setAttribute("disabled", true);
        document.getElementById("btn_send_contact").style.backgroundColor  = '#555555';
    }
}
