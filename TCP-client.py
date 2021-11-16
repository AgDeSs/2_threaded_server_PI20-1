import socket
from time import sleep
userName = input('Пожалуйста, введите имя пользователя: ') + ': '
sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9091))

massage = userName + input(f'{userName}')
while len(massage) != 0:
    sock.send(massage.encode())
    data = sock.recv(1024)
    exit_check = massage.lower()
    if exit_check == 'exit':
        sock.close()
        break
    print(data.decode())
    massage = userName + input(f'{userName}')