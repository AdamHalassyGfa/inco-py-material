import ChatServer

server = ChatServer.ChatServer('192.168.128.65')
server.open()

input("Press Enter to stop.")

server.close()