import socket
def find_service_name():
    protocolname = 'tcp'
    for port in [80,25,53,23,21]:
        print("Port: %s => ServiceName: %s" %(port, socket.getservbyport(port, protocolname)))
if __name__=='__main__':
    find_service_name()