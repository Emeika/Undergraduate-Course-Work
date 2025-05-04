from scapy.all import *
import socket
import sys
import time

###### USAGE
############### sudo python scan4.py ip portLo portHi

def syn_scan(target_ip, port_range):
    ctr = 0  # Counter for closed ports
    cur_time = time.time()
    print("[+] Scanning started at", time.ctime(cur_time))

    for port in port_range:
        # Create SYN packet
        syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        # Send SYN packet and wait for a response
        response = sr1(syn_packet, timeout=1, verbose=0)

        # Analyze the response
        if response:
            if response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x12:  # SYN-ACK flag
                    print(f"tcp/{port} open", end=" | ")

                    # Perform basic banner grabbing
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        sock.connect((target_ip, port))
                        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")  # Generic request
                        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                        sock.close()
                        print(banner.split("\n")[0])  # Print the first line of the banner
                    except Exception as e:
                        print("Unknown version")

                    # Send RST to close the connection
                    rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
                    send(rst_packet, verbose=0)
                elif response.getlayer(TCP).flags == 0x14:  # RST flag
                    ctr += 1
            else:
                print(f"tcp/{port}\t\tfiltered")

    print(f"Closed ports {ctr}")

if __name__ == "__main__":
    # Define target IP and port range
    if len(sys.argv) != 4:
        print("Usage: sudo python scan4.py <target_ip> <port_low> <port_high>")
        sys.exit(1)

    target_ip = sys.argv[1]
    port_low = int(sys.argv[2])
    port_high = int(sys.argv[3])
    port_range = range(port_low, port_high + 1)  # Include the upper bound

    print(f"Starting SYN scan on {target_ip}")
    syn_scan(target_ip, port_range)
