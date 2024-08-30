# This example demonstrates how to test the basic functionality of your scanner to detect live hosts on a network.
import ipaddress
from scapy.all import ICMP, IP, sr1


def ping_ip(ip):
    pkt = IP(dst=str(ip)) / ICMP()
    reply = sr1(pkt, timeout=1, verbose=0)
    return reply is not None


def scan_network(network):
    live_hosts = []
    for ip in ipaddress.IPv4Network(network):
        if ping_ip(ip):
            live_hosts.append(str(ip))
            print(f"{ip} is up")
    return live_hosts


# Example Test
network = "192.168.1.0/24"
live_hosts = scan_network(network)
print(f"Live hosts: {live_hosts}")
