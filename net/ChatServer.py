import random
import socket
import time

import ChatNet
import threading

from socket import *

class ChatServer:

    def __init__(self, server_address):
        self.alive = False
        self.server_address = server_address
        self.discovery_thread = threading.Thread(target=self.push_discovery)
        self.color_thread = threading.Thread(target=self.listen_color)
        self.color_agents = list()

    def color_agent(self, conn):
        name = random.randint(1, 1000)
        while self.alive:
            try:
                msg = conn.recv(1024)
                msg = msg.decode()
                if msg:
                    print(f"Msg: [{msg}]")
                else:
                    time.sleep(1)
            except error as msg:
                print(f"Something went wrong: {msg}")
                break

        print("Agent closed.")

    def listen_color(self):
        color_socket = socket()
        color_socket.bind((self.server_address, ChatNet.CHAT_PORT))
        color_socket.settimeout(5)
        color_socket.setblocking(True)
        color_socket.listen()

        while self.alive:
            try:
                conn, addr = color_socket.accept()
                thread = threading.Thread(target=self.color_agent, args=(conn,))
                print(f"Client from {addr} accepted, starting agent.")
                thread.start()
            except timeout:
                continue
            except error as msg:
                print(f"Listener failed: {msg}")
                self.alive = False
                break

        print("Listener closed.")

    def push_discovery(self):
        discovery_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        discovery_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        discovery_socket.settimeout(0.2)

        while self.alive:
            msg = bytes(self.server_address, 'utf-8')
            discovery_socket.sendto(msg, ('<broadcast>', ChatNet.DISCOVERY_PORT))
            time.sleep(5)
        print("Discovery thread closed.")

    def open(self):
        self.alive = True
        self.discovery_thread.start()
        self.color_thread.start()

    def close(self):
        self.alive = False
        print("I'll close everything...")
