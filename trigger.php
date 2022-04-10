<?php
$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'GET':
        $sh = shell_exec("python3 ListFile.py");
        echo($sh);
        break;
    default:
        $message = "Error send a server method";
        echo($message);
        break;
}

?>