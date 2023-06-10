import ChatClient

print("Searching for server...")
addr = ChatClient.discover()
print(f'Server is {addr}. Connecting...')

client = ChatClient.ChatClient(addr)
client.open()

while True:
    msg = input("Chat# ")
    if msg.startswith('/'):
        if msg.startswith('/name'):
            parts = msg.split(' ')
            client.setName(parts[1])

        elif msg == '/exit':
            break

        else:
            print(f"Invalid command: {msg}")

    else:
        client.send(msg)


client.close()
