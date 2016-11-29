import socket



Home = '192.168.43.211'
MyIP = socket.gethostbyname(socket.gethostname())

if MyIP == Home:
    place = 'Home'
else:
    place = 'Not Home'




