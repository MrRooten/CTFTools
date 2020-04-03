<?php
error_reporting(0);
$s = "当我站在山顶上俯瞰半个鼓浪屿和整个厦门的夜空的时候前几天有人问我你也不说点什么厦门的海风伴着妮妲路过后带来的淅淅沥沥的小雨比起隔壁一家旧中国时期的房子要豪华得多北京的很多东西让我非常丧气远走千里吃豆腐这种理想主义的事情这几年在我身上屡屡发生去年冬天孤身一人来到北京这个古都承载着太多历史的厚重感后来";
$s = str_split($s,2);
$printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c';
$res = Array();
for($i=0;$i < count($s);$i++) {
	var_dump($s[$i]);
}

foreach($res as $key => $value) {
	echo $value;
}
