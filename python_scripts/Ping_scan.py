# This example demonstrates how to test the basic functionality of your scanner to detect live hosts on a network.
import ipaddress
from scapy.all import ICMP, IP, sr1  # type: ignore


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
network = "0.0.0.0/0"  # change your ip accordingly
live_hosts = scan_network(network)
print(f"Live hosts: {live_hosts}")
