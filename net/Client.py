import ChatClient

addr = ChatClient.discover()
print(f'Server is {addr}. Connecting...')

client = ChatClient.ChatClient(addr)
client.open()

while True:
    msg = input("Chat# ")
    if msg == 'exit':
        break
    else:
        client.send(msg)

client.close()
