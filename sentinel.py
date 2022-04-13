import scapy.all as scapy
#from scapy  import Ether, ARP, srp
from NetworkDevicesData import NetworkDevicesData

def main():
    interfaces = scapy.get_if_hwaddr(scapy.conf.iface)
    print(interfaces)
    devicesInfo : list[NetworkDevicesData] = []
    ARPpkt = scapy.Ether(dst='ff:ff:ff:ff:ff')/scapy.ARP(op=1,pdst='192.168.0.1/24')
    received = scapy.srp(ARPpkt,timeout=2,iface=scapy.conf.iface)
    for i in range(len(received[0])):
        devicesInfo.append(NetworkDevicesData(mac=received[0][i].answer.hwsrc,
                                            ip=received[0][i].answer.psrc))
if __name__ == "__main__":
    main()