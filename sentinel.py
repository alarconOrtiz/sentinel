from scapy.all import Ether, ARP,sendp,srp

def main():
    ARPpkt = Ether(dst='ff:ff:ff:ff:ff')/ARP(pdst='192.168.0.1/24', hwsrc="66:66:66:66:66:66")
    ans = sendp(ARPpkt)
    answer, unanswered = srp(ARPpkt)
    for sent, received in answer:
        print(received.sumary())

if __name__ == "__main__":
    main()