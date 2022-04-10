<?php
$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'GET':
        $sh = shell_exec("python3 ListFiles.py");
        echo json_encode($sh);
        break;
    default:
        $message = {'message': "Error send a server method"};
        echo json_encode($message);
        break;
}

?>