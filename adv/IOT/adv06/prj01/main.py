#########################匯入模組#########################
import socket

#########################函式與類別定義#########################


#########################宣告與設定#########################
HOST = "localhost"
PORT = 5438
server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print("server:{} port:P{} start".format(HOST, PORT))
client, addr = server_socket.accept()
print("client address:{}, port:{}".format(addr[0], addr[1]))
#########################主程式#########################
while True:
    msg = client.recv(280).decode("utf8")
    print("Receive Message:" + msg)
    reply = ""

    if msg == "hi":
        reply = "Hello!"
        client.send(reply.encode("utf8"))
    elif msg == "bye":
        reply = "Goodbye!"
        client.send(b"quit")
        break
    else:
        reply = "wtf"
        client.send(reply.encode("utf8"))

client.close()
server_socket.close()
