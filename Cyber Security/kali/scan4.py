from scapy.all import *
import socket
import time
import sys
from datetime import datetime


def get_service_name(port):
    """
    Get the service name for a given port.
    """
    CUSTOM_SERVICES = {
        21: "ftp",
        22: "ssh",
        23: "telnet",
        25: "smtp",
        53: "domain",
        80: "http",
        110: "pop3",
        139: "netbios-ssn",
        443: "https",
        445: "microsoft-ds",
        135: "msrpc",
        8834: "netbios-ssn",
    }
    return CUSTOM_SERVICES.get(port, "unknown")


def banner_grab(target_ip, port):
    """
    Attempts to grab the banner of the service running on the specified port.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((target_ip, port))
            if port == 80 or port == 443:  # HTTP or HTTPS
                s.sendall(b"HEAD / HTTP/1.1\r\nHost: %s\r\n\r\n" % target_ip.encode())
            elif port in [21, 22, 23, 25]:  # FTP, SSH, Telnet, SMTP
                pass  # Services usually provide banners automatically
            response = s.recv(1024).decode().strip()
            return response
    except Exception as e:
        return "Unknown version"


def syn_scan(target_ip, port_range):
    """
    Perform a SYN scan to detect open ports and retrieve banners.
    """
    start_time = time.time()
    print(f"Starting scan on {target_ip}")
    print(f"[+] Scanning started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'PORT':<12}{'STATE':<10}{'SERVICE':<15}{'BANNER':<40}{'RESPONSE TIME (ms)':<20}")
    print("-" * 80)

    open_ports = []
    closed_ports = 0

    for port in port_range:
        # Record start time for response timing
        port_start_time = time.time()

        # Create SYN packet
        syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        response = sr1(syn_packet, timeout=1, verbose=0)

        # Calculate response time
        response_time = round((time.time() - port_start_time) * 1000, 2)  # in milliseconds

        # Get service name
        service = get_service_name(port)

        if response:
            if response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x12:  # SYN-ACK flag
                    # Grab banner for open port
                    banner = banner_grab(target_ip, port)
                    print(f"tcp/{port:<8}{'open':<10}{service:<15}{banner:<40}{response_time:<20}")
                    open_ports.append(port)

                    # Send RST to close the connection
                    rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
                    send(rst_packet, verbose=0)
                elif response.getlayer(TCP).flags == 0x14:  # RST flag
                    closed_ports += 1
        else:
            closed_ports += 1

    end_time = time.time()
    print("\n[+] Scanning completed at", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(f"[+] Scan duration: {round(end_time - start_time, 2)} seconds")
    print(f"[+] Open ports: {len(open_ports)}")
    print(f"[+] Closed ports: {closed_ports}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: sudo python scanner.py <ip> <portLo> <portHi>")
        sys.exit(1)

    target_ip = sys.argv[1]
    port_low = int(sys.argv[2])
    port_high = int(sys.argv[3])
    port_range = range(port_low, port_high + 1)

    print(f"Starting SYN scan on {target_ip}")
    syn_scan(target_ip, port_range)
