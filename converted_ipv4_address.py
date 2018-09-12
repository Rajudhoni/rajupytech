import socket
from binascii import hexlify
def converted_ip_adress():
    for ip_addr in  ['127.0.0.1','192.168.0.2']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip = socket.inet_ntoa(packed_ip_addr)
        print("IP Adress: %s => Packed: %s, unpacked: %s" %(ip_addr,hexlify(packed_ip_addr),unpacked_ip))
if __name__=='__main__':
    converted_ip_adress()