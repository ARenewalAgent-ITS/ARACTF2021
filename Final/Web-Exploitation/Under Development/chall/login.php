<?php 
    session_start();
    if (isset($_POST['login'])) {
        if (isset($_POST["username"]) && isset($_POST["password"])) {
            $username = $_POST['username'];
            $password = $_POST['password'];
            if ($username == "adm0000000n" && $password == "zuuup33r_S3cret_p@@ssword") {
                $_SESSION["username"] = "adm0000000n";
                $_SESSION["password"] = "zuuup33r_S3cret_p@@ssword";
                header("Location: index.php");
            }else {
                $message = "( ͡◉ ͜ʖ ͡◉)";
            }
        }else {
            $message = "( ͡◉ ͜ʖ ͡◉)";
        }
    }

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>( ͡◉ ͜ʖ ͡◉)</title>
    <link rel="stylesheet" href="assets/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="assets/main.css"/>
    <script src="assets/jquery-3.6.0.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
</head>
<body>


<!-- content -->
<div class="col-lg-12 d-flex justify-content-center mt-5">
<div class="col-lg-4 d-flex justify-content-center text-center">
    <form class="form-signin" method="POST" action="">
      <img class="mb-4" src="assets/images/autoindex.png" alt="" width="100" height="100">
      <h1 class="h3 mb-3 font-weight-normal">Under Development</h1>
      <div class="mb-2">
      <label for="username" class="sr-only">Username</label>
      <input type="text" name="username" id="username" class="form-control" placeholder="Username" autocomplete="off" required autofocus>
      </div>
      <div class="mb-2">
      <label for="password" class="sr-only">Password</label>
      <input type="password" name="password" id="password" class="form-control" placeholder="Password" autocomplete="off" required>
      </div>
      <button class="btn btn-lg btn-primary btn-block" type="submit" name="login">Sign in</button>
      <?php 
        if (isset($message)) {
            echo "<br><p> $message </p>";
        }
        ?>
    </form>

</div>
</div>
<!-- content end -->


        <!-- footer -->
        <footer class="fixed-bottom bg-light text-center text-white mt-5">
  <!-- Copyright -->
  <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
    © 2021 Copyright:
    <a class="text-white" href="https://arek.its.ac.id/ara/">adm0000000n</a>
  </div>
  <!-- Copyright -->
</footer>
        <!-- footer end -->
</body>
</html>