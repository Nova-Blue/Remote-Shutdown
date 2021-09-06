from cryptography.fernet import Fernet
import socket
import os

def _start_server(port, key_location):

    #bind socket and wait
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    client, addr = s.accept()

    msg = client.recv(5000)

    #retreive encryption key
    keyfile = open(key_location, mode='rb')
    key = keyfile.read()
    keyfile.close()

    #decrypt
    fernet = Fernet(key)
    recv_text = fernet.decrypt(msg).decode()

    client.close()
    s.close()

    if(recv_text == 'SHUTDOWN'):
        os.system('shutdown /p')

def _parse_config_file():
    parameters_read = 0
    
    f = open('RSDServerConfig.txt', 'r')

    for line in f:
        line = line.strip()
        if (line.startswith('#') or len(line) == 0):
            continue

        if parameters_read == 0:
            port = int(line)
        elif parameters_read == 1:
            key_location = line

        parameters_read += 1

    f.close()

    return port, key_location

    

port, key_location = _parse_config_file()
_start_server(port, key_location)
