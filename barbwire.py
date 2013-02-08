import sys
import socket
from binary_tools import to_hex
from pcapfile import savefile

_UDP_HEADER_LEN = 42

def read_file(filename):
    capfile = savefile.load_savefile(open(filename, 'r'))
    return capfile

def playback_packets_to_server(capfile, server_ip, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((server_ip, int(server_port)))
    for packet in capfile.packets:
        print packet.packet_len
        print packet.packet
        print to_hex(packet.raw()[_UDP_HEADER_LEN:])
        s.send(packet.raw()[_UDP_HEADER_LEN:])

if __name__ == '__main__':
    capfile = read_file(sys.argv[1])
    playback_packets_to_server(capfile, sys.argv[2], sys.argv[3])
    