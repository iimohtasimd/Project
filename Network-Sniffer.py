from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime
import ipaddress  # better IP handling

def get_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "Other"

# Improved direction logic using ipaddress
def get_direction(src_ip):
    try:
        if ipaddress.ip_address(src_ip).is_private:
            return "Outgoing"
        else:
            return "Incoming"
    except:
        return "Unknown"

def process_packet(packet):
    if packet.haslayer(IP):
        ip = packet[IP]
        time_now = datetime.now().strftime("%H:%M:%S")

        print("\n" + "-"*40)
        print(f"Time            : {time_now}")
        print(f"Direction       : {get_direction(ip.src)}")
        print(f"Source IP       : {ip.src}")
        print(f"Destination IP  : {ip.dst}")
        print(f"Protocol        : {get_protocol(packet)}")

        # Payload handling
        if packet.haslayer(Raw):
            print(f"Payload         : {packet[Raw].load[:50]}")
        else:
            print("Payload         : Not visible (possibly encrypted)")

        print("-"*40)

print("🔍 Sniffer running... Press CTRL+C to stop\n")

sniff(prn=process_packet, store=False)