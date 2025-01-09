import socket, threading
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7976))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICKNAME":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An eroor occured!")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()