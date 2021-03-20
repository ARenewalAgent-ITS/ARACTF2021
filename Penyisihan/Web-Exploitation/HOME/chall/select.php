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
    <title>HOME</title>
  </head>
  <body>
    <center>
    <h1>MY ROOM</h1>
    <?php 
        if (isset($_GET['room'])) {
            $room = $_GET['room'];
            if ($room != "kitchen.php" && $room != "livingroom.php" && $room != "bedroom.php") {
              $room = str_replace( array( "../","txt"), "", $room );
            }
              
              include "$room";
        }else {
          header('Location: index.php');
        }
    
    
    ?>

</center>
  </body>
</html>
<?php 
} else {
  echo("Your IP address is not allowed.");
  echo("<h5>Stand Your Ground, Keep Going FORWARD</h5>");
}

?>