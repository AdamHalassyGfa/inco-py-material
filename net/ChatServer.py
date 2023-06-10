import random
import socket
import time

import ChatNet
import threading

from socket import *


class ChatAgent:
    def __init__(self, parent, conn):
        self.alive = True
        self.parent = parent
        self.conn = conn
        self.name = f"AG-{random.randint(1000, 9999)}"

    def listen(self):
        self.parent.sendall(self, f"[{self.name}] joined to the chat.")
        while self.alive:
            try:
                msg = self.conn.recv(1024)
                if not msg:
                    break

                msg = msg.decode()
                if msg:
                    self.handle(msg)
                else:
                    time.sleep(1)
            except error as msg:
                if self.alive:
                    print(f"Something went wrong: {msg}")
                break

        self.parent.sendall(self, f"{self.name} left the chat.")
        self.parent.remove(self)
        print("Agent closed.")

    def handle(self, msg):
        parts = msg.split(':')
        cmd = parts[0]
        body = parts[1]
        if cmd == 'name':
            oldName = self.name
            self.name = body
            print(f"[{oldName}] now ['{body}']")
            self.parent.sendall(self, f"'{oldName}' renamed to '{body}'.")
        elif cmd == 'msg':
            print(f"[{self}] said: '{body}'")
            self.parent.sendall(self, body)

    def send(self, sender, msg):
        if sender != self:
            self.conn.sendall(bytes(msg, 'utf-8'))

    def close(self):
        self.alive = False


class ChatServer:

    def __init__(self, server_address):
        self.alive = False
        self.server_address = server_address
        self.discovery_thread = threading.Thread(target=self.push_discovery)
        self.color_thread = threading.Thread(target=self.listen_color)
        self.agents = list()

    def listen_color(self):
        color_socket = socket()
        color_socket.bind((self.server_address, ChatNet.CHAT_PORT))
        color_socket.settimeout(5)
        color_socket.setblocking(True)
        color_socket.listen()

        while self.alive:
            try:
                conn, addr = color_socket.accept()
                agent = ChatAgent(self, conn)
                self.agents.append(agent)
                thread = threading.Thread(target=agent.listen)
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
        agents = self.agents.copy()
        for agent in agents:
            agent.stop()
        print("I'll close everything...")

    def sendall(self, sender, msg):
        agents = self.agents.copy()
        msg = f"{sender.name}> {msg}"
        for agent in agents:
            agent.send(sender, msg)

    def remove(self, agent):
        self.agents.remove(agent)
