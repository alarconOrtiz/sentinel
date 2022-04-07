from scapy.all import Ether, ARP,sendp,srp

def main():
    ARPpkt = Ether(dst='ff:ff:ff:ff:ff')/ARP(op=1,pdst='192.168.0.1/24')
    received = srp(ARPpkt,timeout=2,iface="en0")
    for i in range(len(received[0])):
        print(received[0][i].answer.hwsrc)
        print(received[0][i].answer.psrc)

if __name__ == "__main__":
    main()