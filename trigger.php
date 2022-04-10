<?php
$method = $_SERVER['REQUEST_METHOD'];
header("Access-Control-Allow-Origin: *");
switch ($method) {
    case 'GET':
        $sh = shell_exec("python3 ListFiles.py");
        echo $sh;
        break;
}

?>