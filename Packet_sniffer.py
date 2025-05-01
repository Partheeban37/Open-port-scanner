import socket # Importing the socket library
from scapy.all import * # Importing all functions from the Scapy library
from scapy.layers.l2 import Ether # Importing the Ether class from Scapy for Ethernet layer packet manipulation

sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCKET_RAW, socket.ntohs(3)) # Creating a raw socket to capture packets
interface = "eth2" # Network interface to capture packets on
sniffer_socket.bind((interface, 0)) # Binding the socket to the specified interface

try:
    while True:
        raw_data, addr = sniffer_socket.recvfrom(65535) # Receiving raw packet data
        packet = Ether(raw_data) # Creating an Ether object from the raw data
        print(packet.summary())
        # print(packet.show()) # Uncomment to display detailed packet information   
        
except KeyboardInterrupt:
    sniffer_socket.close() # Closing the socket on keyboard interrupt
    print("\nSniffer stopped.")