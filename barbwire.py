import sys
from binary_tools import to_hex
from pcapfile import savefile

_UDP_HEADER_LEN = 42

def read_file(filename):
    file = open(filename, 'r')
    capfile = savefile.load_savefile(file)
    for packet in capfile.packets:
        print packet.packet_len
        print packet.packet
        print packet.packet[2*_UDP_HEADER_LEN:]
        print to_hex(packet.raw()[_UDP_HEADER_LEN:])


if __name__ == '__main__':
    read_file(sys.argv[1])