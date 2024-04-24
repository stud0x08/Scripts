import nmap

print("Simple NMAP automation tool\n"
      "Designed by ----------------Ankit Sinha---------------------------\n")
scan = nmap.PortScanner()
host = input("Enter the target IP: ")

resp = input("Enter the type of scan you want to run: \n"
            "1. SYN scan\n"
            "2. UDP scan\n:")

if resp == '1':
    print("Nmap Version: ",scan.nmap_version())
    scan.scan(host,'1-65535','-v -sS')
    print("IP Status: " ,scan[host].state())
    print(scan[host].all_protocols())
    print("Open port: " ,scan[host]['tcp'].keys())
if resp == '2':
    print("Nmap Version: ", scan.nmap_version())
    scan.scan(host, '1-1000', '-v -sU')
    print("IP Status: ", scan[host].state())
    print(scan[host].all_protocols())
    print("Open ports: ", scan[host]['udp'].keys())
else:
    exit()