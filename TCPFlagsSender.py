# Copyright
# Original author: Edino De Souza
# Repository: https://github.com/edino/TCPFlagsSender
# License: GPL-3.0 license - https://github.com/edino/TCPFlagsSender/tree/main?tab=GPL-3.0-1-ov-file
# Description: This script allows users to customize and send TCP packets with specific flags, IP addresses, ports, and quantities.

# BuildDate: 5:10 PM EST 2024-01-13

# A simple way to execute this script is using the following command: curl -s https://raw.githubusercontent.com/edino/TCPFlagsSender/main/TCPFlagsSender.py | python -

from scapy.all import IP, TCP, send

# Function to get user input for TCP flags
def get_tcp_flags():
    print("TCP Flags Menu:")
    print("")
    print("1. URG - (Urgent): TCP Urgent Flag signals meaningful Urgent Pointer, prompting the receiver to accept urgent data; its absence implies no outstanding urgency.")
    print("")
    print("2. ACK - (Acknowledgment): Confirms the connection agreement has been accepted and that the connection is now established. At this point data transfer can begin.")
    print("")
    print("3. PSH - (Push): Sends data immediately.")
    print("")
    print("4. RST - (Reset): Closes the session without waiting for a response. This may be because an unexpected packet was received.")
    print("")
    print("5. SYN - (Synchronization): A request for synchronization")
    print("")
    print("6. FIN - (Finish): Request to end the session. The connection is closed when both devices accept this.")
    print("")
    
    # Get user input for TCP flags
    selected_flags = input("Enter the numbers of TCP flags (comma-separated): ")
    selected_flags = selected_flags.split(',')
    
    # Map user input to corresponding TCP flags
    flags_mapping = {'1': 'URG', '2': 'ACK', '3': 'PSH', '4': 'RST', '5': 'SYN', '6': 'FIN'}
    tcp_flags = [flags_mapping.get(flag.strip()) for flag in selected_flags if flag.strip() in flags_mapping]
    
    return ','.join(tcp_flags)

# Get user input for source and destination IP addresses
src_ip = input("Enter source IP address: ")
dst_ip = input("Enter destination IP address: ")

# Get user input for source and destination ports
src_port = int(input("Enter source port: "))
dst_port = int(input("Enter destination port: "))

# Get user input for TCP flags
tcp_flags = get_tcp_flags()

# Create an IP packet
ip_packet = IP(src=src_ip, dst=dst_ip)

# Create a TCP packet with the specified flags
tcp_packet = TCP(sport=src_port, dport=dst_port, flags=tcp_flags)

# Combine the IP and TCP packets
packet = ip_packet / tcp_packet

# Get user input for the number of packets to send
num_packets = int(input("Enter the number of packets to send: "))

# Send packets in a loop
for _ in range(num_packets):
    send(packet)
