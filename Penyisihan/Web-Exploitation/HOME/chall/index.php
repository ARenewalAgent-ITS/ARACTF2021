<?php 
  include 'function.php';
  $ip = get_ip();


if ($ip == "127.0.0.1") {

?>
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style/style.css">
    <!-- Bootstrap CSS -->
    <title>HOME</title>
  </head>
  <body>
    <center style="margin-bottom:30px">
    <h1>HOME</h1>
    <img src="images/home.jpg" alt="" style="height: 400px; width:auto">

    <h5 class="card-title">Kitchen</h5>
        <a href="select.php?room=kitchen.php" class="btn btn-primary">Go</a>

    <h5 class="card-title">Living Room</h5>
        <a href="select.php?room=livingroom.php" class="btn btn-primary">Go</a>

    <h5 class="card-title">Bedroom</h5>
        <a href="select.php?room=bedroom.php" class="btn btn-primary">Go</a>

  </center>
  </body>
</html>
<?php 
} else {
  echo("Your IP address is not allowed.");
  echo("<h5>Stand Your Ground, Keep Going FORWARD</h5>");
}

?>