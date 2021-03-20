<?php

class Token{
    public $username;
    public $password;
}

function flag($token){
    $pass_verif = "\}Fr@!-a";
    if($token->username == 'admin'){
        if(strlen($token->password)>strlen($pass_verif)){
            if(hash('sha256',$token->password) == hash('sha256',$pass_verif)){
                echo 'ara2021{cl4551c_typ3_ju66ling}';
            }
            else{
                echo 'Burn your oven';
            }
        }
        else{
            echo 'Baking in progress';
        }
    }
    else{
        echo 'No Flag for you. Sadge :(';
    }
}


if(!isset($_COOKIE['bake_here'])){
    $token = new Token;
    $token->username = 'user';
    $token->password = 'user';
    $cookies = base64_encode(serialize($token));
    setcookie('bake_here',$cookies);
    echo "Preparing your oven ......";
}
else{
    flag(unserialize(base64_decode($_COOKIE['bake_here'])));
}
?>