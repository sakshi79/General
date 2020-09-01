import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('facebook.com', 443))
cmd = 'GET https://www.facebook.com/sakshi.b.58367/about?lst=100025855030063%3A100025855030063%3A1591819708 HTTPS/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()