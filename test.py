from lib.net.http.httpclient import HttpClientAsync

client = HttpClientAsync(["https://0.0.0.0:4443/login" for i in range(30)],method="post",data="abcdefg")
client.sendall(print)