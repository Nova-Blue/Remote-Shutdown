from cryptography.fernet import Fernet
import socket

def shutdown():

    port, ip_addr, key_location = _parse_config_file()
    
    #connect socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_addr, port))

    #retreive encryption key
    keyfile = open(key_location, mode='rb')
    key = keyfile.read()
    keyfile.close()

    #encrypt and send
    fernet = Fernet(key)
    msg = fernet.encrypt(b'SHUTDOWN')
    s.sendall(msg)
    
    s.close()

def _parse_config_file():
    parameters_read = 0
    
    f = open('ClientConfig.txt', 'r')

    for line in f:
        line = line.strip()
        if (line.startswith('#') or len(line) == 0):
            continue

        if parameters_read == 0:
            port = int(line)
        elif parameters_read == 1:
            ip_addr = line
        elif parameters_read == 2:
            key_location = line

        parameters_read += 1

    f.close()

    return port, ip_addr, key_location
