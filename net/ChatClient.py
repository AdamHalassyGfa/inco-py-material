import random
import sys
import threading
import time

import ChatNet

from socket import *


def discover():
    discovery = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    discovery.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    discovery.bind(("", ChatNet.DISCOVERY_PORT))
    resp = discovery.recv(1024)
    return resp.decode()


class ChatClient:
    def __init__(self, address):
        self.name = f"CL-{random.randint(1000, 9999)}"
        self.address = address
        self.socket = socket()
        self.alive = False

    def listen(self):
        while self.alive:
            try:
                msg = self.socket.recv(1024)
                if not msg:
                    break

                msg = msg.decode()
                if msg:
                    print(f"\n{msg}\nChat# ", end='')
                else:
                    time.sleep(1)
            except error as msg:
                if self.alive:
                    print(f"Something went wrong: {msg}")
                break

        print("Client closed.")
        sys.exit(0)

    def close(self):
        self.alive = False
        self.socket.shutdown(SHUT_RDWR)
        self.socket.close()

    def open(self):
        self.socket.connect((self.address, ChatNet.CHAT_PORT))
        self.alive = True
        thread = threading.Thread(target=self.listen)
        thread.start()

    def send(self, msg):
        msg = f"msg:{msg}"
        self.socket.sendall(bytes(msg, 'utf-8'))

    def setName(self, name):
        self.name = name
        self.socket.sendall(bytes(f"name:{name}", "utf-8"))
