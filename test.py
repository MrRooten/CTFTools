from lib.http.httpclient import HttpClientAsync

client = HttpClientAsync(["https://www.baidu.com" for i in range(30)],method="get",params="3=3")
client.sendall(print)