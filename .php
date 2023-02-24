$data = array(
    'foo' => 'bar',
    'baz' => 'qux'
);

$url = 'http://localhost:5000/my-route';

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
