import socket

def retbanner(ip,port):
    try:
        s = socket.socket()
        s.connect((ip,port))
        s.settimeout(1)
        banner = s.recv(4096)
        return banner
    except:
        return

def main():
    ip =input("Enter the target to scan: ")
    for port in range(1,30):
        banner = retbanner(ip,port)
        if banner:
            print(ip, ":" , port , ":" , banner)
main()
