# Copyright
# Original author: Edino De Souza
# Repository: https://github.com/edino/TCPFlagsSender
# License: GPL-3.0 license - https://github.com/edino/TCPFlagsSender/tree/main?tab=GPL-3.0-1-ov-file
# Description: This script allows users to customize and send TCP packets with specific flags, IP addresses, ports, and quantities.

# BuildDate: 5:53 PM EST 2024-01-13

# A simple way to execute this script is using the following command: curl -s https://raw.githubusercontent.com/edino/TCPFlagsSender/main/tcp_flags_sender.py | python3 -

from scapy.all import IP, TCP, send

# Function to get user input for TCP flags
def get_tcp_flags():
    print("")
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
    selected_flags = input("\nEnter the numbers of TCP flags (comma-separated): ")
    selected_flags = selected_flags.split(',')

    # Map user input to corresponding TCP flags
    flags_mapping = {'1': 'U', '2': 'A', '3': 'P', '4': 'R', '5': 'S', '6': 'F'}
    tcp_flags = [flags_mapping.get(flag.strip()) for flag in selected_flags if flag.strip() in flags_mapping]

    return ''.join(tcp_flags)
    
# Initialize variables
src_ip, dst_ip, src_port, dst_port = None, None, None, None

# Run the script in a loop based on user input
while True:
    # Get user input for source and destination IP addresses if not already stored
    if src_ip is None:
        src_ip = input("\nEnter source IP address: ")
    if dst_ip is None:
        dst_ip = input("\nEnter destination IP address: ")

    # Get user input for source and destination ports if not already stored
    if src_port is None:
        src_port = int(input("\nEnter source port: "))
    if dst_port is None:
        dst_port = int(input("\nEnter destination port: "))

    # Get user input for TCP flags
    tcp_flags = get_tcp_flags()

    # Create an IP packet
    ip_packet = IP(src=src_ip, dst=dst_ip)

    # Create a TCP packet with the specified flags
    tcp_packet = TCP(sport=src_port, dport=dst_port, flags=tcp_flags)

    # Combine the IP and TCP packets
    packet = ip_packet / tcp_packet

    # Get user input for the number of packets to send
    num_packets = int(input("\nEnter the number of packets to send: "))

    # Send packets in a loop
    for _ in range(num_packets):
        send(packet)

    # Ask the user if they want to run the script again with the same inputs
    run_again = input("\nDo you want to run the script again with the same inputs? (yes/no): ").lower()
    if run_again != 'yes':
        break
