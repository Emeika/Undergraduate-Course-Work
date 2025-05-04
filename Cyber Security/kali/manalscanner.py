from scapy.all import *
import socket
import sys
import time


def banner_grab(ip, port):
    """Grab service banners for the given IP and port."""
    try:
        # Create a socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Timeout increased to 5 seconds
        s.connect((ip, port))

        # Don't send anything for FTP to allow the server to respond
        if port == 21:  # FTP
            response = s.recv(4096).decode('utf-8', errors='ignore')
            s.close()
            return response.strip()

        # Send a request based on the port
        if port == 80:  # HTTP
            s.send(b"GET / HTTP/1.1\r\nHost: " + bytes(ip, 'utf-8') + b"\r\n\r\n")
        elif port == 22:  # SSH
            # Don't send data; just receive the banner
            pass
        else:
            s.send(b"\r\n")  # Generic request for other services

        # Receive and return the banner
        banner = s.recv(4096).decode('utf-8', errors='ignore')
        s.close()

        # For HTTP, filter the response to show only headers
        if port == 80:
            header_lines = []
            for line in banner.split("\n"):
                header_lines.append(line.strip())
                if "Content-Type" in line:
                    break
            return "\n".join(header_lines)

        # For SSH, suppress "Protocol mismatch" and return the actual banner
        if port == 22 and "Protocol mismatch" in banner:
            return banner.split("\n")[0].strip()

        return banner.strip() if banner else "Unknown version"
    except Exception:
        return "Unknown version"


def get_service_name(port):
    """Return the service name based on the port number."""
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "Unknown service"


def syn_scan(ip, port_range):
    """Perform SYN scan, grab banners, and display service names."""
    print(f"[+] Scanning started at {time.ctime()}")
    closed_ports = 0  # Counter for closed ports
    open_ports = 0  # Counter for open ports

    for port in port_range:
        # Create SYN packet
        syn_packet = IP(dst=ip) / TCP(dport=port, flags="S")

        # Send SYN packet and wait for response
        response = sr1(syn_packet, timeout=1, verbose=0)

        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:  # SYN-ACK received
            # Port is open
            open_ports += 1
            service_name = get_service_name(port)
            print(f"tcp/{port:<5} open | {service_name}", end=" | ")

            # Grab the service banner
            banner = banner_grab(ip, port)
            if banner:
                print(banner)
            else:
                print("Unknown version")

            # Send RST packet to close connection
            rst_packet = IP(dst=ip) / TCP(dport=port, flags="R")
            send(rst_packet, verbose=0)
        else:
            # Port is closed or filtered
            closed_ports += 1

    print(f"\n[+] Total closed ports: {closed_ports}")


if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) < 4:
        print("Usage: python scanner.py <target_ip> <low_port> <high_port>")
        sys.exit(1)

    target_ip = sys.argv[1]
    port_low = int(sys.argv[2])
    port_high = int(sys.argv[3])
    port_range = range(port_low, port_high + 1)

    # Start the SYN scan
    print(f"Starting scan on {target_ip}")
    syn_scan(target_ip, port_range)
