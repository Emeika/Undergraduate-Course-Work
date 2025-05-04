from scapy.all import *
import socket
import sys
import time

###### USAGE
############### sudo python task1.py ip portLo portHi
def syn_scan(target_ip, port_range):
    ctr = 0
    cur_time = time.time()
    print("[+] Scanning started at", time.ctime(cur_time))

    # Define known services for common ports
    known_services = {
        21: "ftp",
        22: "ssh",
        23: "telnet",
        25: "smtp",
        53: "domain",
        80: "http",
        111: "sunrpc",
        139: "netbios-ssn",
        445: "microsoft-ds",
    }

    for port in port_range:
        # Create SYN packet
        syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

        # Send SYN packet and wait for a response
        response = sr1(syn_packet, timeout=1, verbose=0)

        # Analyze the response
        if response:
            if response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x12:  # SYN-ACK flag
                    # Print the open port and service
                    service = known_services.get(port, "Unknown service")
                    print(f"tcp/{port:}open | {service}", end=" | ")

                    # Attempt to grab the service banner
                    try:
                        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        soc.settimeout(1)
                        soc.connect((target_ip, port))

                        # Handle service-specific banners
                        if port == 21:  # FTP
                            soc.send(b"USER anonymous\r\n")
                        elif port == 80:  # HTTP
                            soc.send(b"HEAD / HTTP/1.0\r\n\r\n")

                        # Generic banner retrieval
                        banner = soc.recv(1024).decode('utf-8', errors='ignore').strip()
                        soc.close()
                        if banner:
                            print(banner.split("\n")[0], end="")
                        else:
                            print("No banner received", end="")
                    except Exception:
                        print("Banner not retrievable", end="")

                    print()  # Move to the next line after printing the banner

                    # Send RST to close the connection
                    rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
                    send(rst_packet, verbose=0)

                elif response.getlayer(TCP).flags == 0x14:  # RST flag
                    ctr += 1

        else:
            print(f"tcp/{port:<6}filtered")

    print("Closed ports", ctr)


if __name__ == "__main__":
    # Define target IP and port range
    if len(sys.argv) < 4:
        print("Usage: sudo python task1.py <ip> <portLo> <portHi>")
        sys.exit(1)

    target_ip = sys.argv[1]
    port_low = int(sys.argv[2])
    port_high = int(sys.argv[3])
    port_range = range(port_low, port_high)  # Ports range
    print(f"Starting SYN scan on {target_ip}")
    syn_scan(target_ip, port_range)
