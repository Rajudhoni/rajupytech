import socket
def print_machine_info():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print("HOSTNAME: %s\n" %hostname)
    print("IP_ADDRESS: %s" %ipaddress)
    
if __name__=='__main__':
    print_machine_info()
    