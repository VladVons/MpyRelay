#!/usr/bin/python

import socket


def Server(aPort, aTimeOut = 1): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')
 
    # Bind socket to local host and port
    try:
        s.bind(('', aPort))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        return
 
    #Start listening on socket
    s.settimeout(aTimeOut)
    s.listen(10)
    print('Socket now listening on port %s' % aPort)
 
    #now keep talking with the client
    Cnt = 0
    while True:
        try:
            conn, addr = s.accept()
        except socket.timeout:
            continue

        Cnt += 1
        Replay = 'Count ' + str(Cnt)

        #Receiving from client
        conn.settimeout(aTimeOut)
        try:
            data = conn.recv(1024)
        except socket.timeout:
            continue

        #print('data', data)
        if (not data): 
            continue

        print(data)
        #Reply = Replay + ' -> ' + data 
        conn.sendall(bytearray(Replay, 'utf8'))

    s.close()

Server(8080)
