import ChatNet

from socket import *


def discover():
    discovery = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    discovery.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    discovery.bind(("", ChatNet.DISCOVERY_PORT))
    print('Awaiting response...')
    resp = discovery.recv(1024)
    return resp.decode()


class ChatClient:
    def __init__(self, address):
        self.address = address
        self.socket = socket()

    def close(self):
        self.socket.shutdown(SHUT_RDWR)
        self.socket.close()

    def open(self):
        self.socket.connect((self.address, ChatNet.CHAT_PORT))

    def send(self, msg):
        self.socket.sendall(bytes(msg, 'utf-8'))
