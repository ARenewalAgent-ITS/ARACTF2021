<?php 
    session_start();
    if (!$_SESSION['username'] == "adm0000000n" && !$_SESSION['password'] == "zuuup33r_S3cret_p@@ssword") {
      header("Location: login.php");
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
<!-- navbar -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="index.php">MyAlbum</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item ">
        <a class="nav-link" href="index.php">Home </a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="mybest.php">zup33r zecr33t <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="logout.php">Logout</a>
      </li>
  </div>
</nav>
<!-- content -->
<div class="col-lg-12 d-flex justify-content-center text-center mt-5">
<h1>Best Picture</h1>
</div>
<div class="col-lg-12 d-flex justify-content-center text-center mt-3 mb-5">
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      
    </div>
    <div class="flip-card-back">
      <h1>FLAG</h1>
      <p>/flag.txt</p>
    </div>
  </div>
</div> 
</div>
<!-- content end -->

<!-- navbar end -->
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