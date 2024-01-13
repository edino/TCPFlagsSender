# TCPFlagsSender

This Python code uses the Scapy library to construct and send custom TCP packets based on user input. Here's a step-by-step explanation:

Import Necessary Modules:

from scapy.all import IP, TCP, send
Imports the required classes and functions from the Scapy library, including IP, TCP, and send.

Define Function to Get TCP Flags:

def get_tcp_flags():
Presents a menu of TCP flags to the user, explaining each flag's purpose. Then, it takes user input for the desired TCP flags.

Get User Input for IP Addresses and Ports:

src_ip = input("Enter source IP address: ")
dst_ip = input("Enter destination IP address: ")
src_port = int(input("Enter source port: "))
dst_port = int(input("Enter destination port: "))
Collects user input for source and destination IP addresses, as well as source and destination ports.

Get User Input for TCP Flags:

tcp_flags = get_tcp_flags()
Calls the get_tcp_flags function to obtain user input for TCP flags.

Create IP and TCP Packets:

ip_packet = IP(src=src_ip, dst=dst_ip)
tcp_packet = TCP(sport=src_port, dport=dst_port, flags=tcp_flags)
Constructs IP and TCP packets using the Scapy library, with specified source and destination IP addresses, ports, and TCP flags.

Combine IP and TCP Packets:

packet = ip_packet / tcp_packet
Combines the IP and TCP packets to form a complete packet.

Get User Input for Number of Packets:

num_packets = int(input("Enter the number of packets to send: "))
Collects user input for the number of packets to send.

Send Packets in a Loop:


for _ in range(num_packets):
    send(packet)
	
Sends the constructed packet in a loop based on the user-specified number of packets using the send function from Scapy.

Overall, this script allows users to customize and send TCP packets with specific flags, IP addresses, ports, and quantities.
