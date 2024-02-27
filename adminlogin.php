<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login</title>
</head>
<body>
    <?php
    // Include the config file
    require_once 'config.php';

    // Check if the user submitted the form
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Get the username and password from the form
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Check if the username and password match
        if ($username == $admin_username && password_verify($password, $admin_password)) {
            // Password is correct, redirect to admin page
            header("Location: admin.php");
        } else {
            // Incorrect username or password
            echo "<p>Incorrect username or password</p>";
        }
    }
    ?>

    <h1>Admin Login</h1>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
