<?php

$items = [
    ['user-id' => 1, 'likes' => 1, 'dislikes' => 2],
    ['user-id' => 1, 'likes' => 2, 'dislikes' => 3],
    ['user-id' => 2, 'likes' => 3, 'dislikes' => 4]
];

$res = [];
$init = ['likes' => 0, 'dislikes' => 0];
foreach($items as $item){
    $key = $item['user-id'];
    $res[$key] = $res[$key] ?? $init;
    $res[$key]['likes']    += $item['likes'];
    $res[$key]['dislikes'] += $item['dislikes'];
}

echo json_encode($res), PHP_EOL;
