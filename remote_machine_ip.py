import socket
def get_remote_machine():
    remotehost = "www.ipl.com"
    try:
        print("IP ADDRESS OF %s : %s" %(remotehost,socket.gethostbyname(remotehost)))
    except socket.error as err_msg:
        print("%s : %s " %(remotehost,err_msg))
if __name__=='__main__':
    get_remote_machine()
