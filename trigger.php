<?php
$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'GET':
        $sh = shell_exec("python3 ListFiles.py");
        echo $sh;
        break;
}

?>