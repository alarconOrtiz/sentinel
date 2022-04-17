import logging 
from datetime import datetime
import scapy.all as scapy
from NetworkDevicesData import NetworkDevicesData
from ConfigHandler import ConfigHandler

def convertDic2NetworkDevicesData(devicesKnown : dict) -> list():
    devicesList = list()
    
    for key in devicesKnown:
        NetDevice = NetworkDevicesData( ip = devicesKnown[key][1], mac = devicesKnown[key][0], alias = devicesKnown[key][2])
        devicesList.append(NetDevice)

    logging.debug(f'devices read from a file : {devicesList}')
    return devicesList

def main():
    logName = f'sentinel{datetime.now().strftime("_%y_%m_%d")}.log'
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)#,filename=logName) 
    logging.info(f'Init app log {logName}')
    #get file info
    config = ConfigHandler()
    config.setConfigFile("/Users/alarcon/Documents/GitHub/sentinel/sentinel.ini")
    devicesknownDic = config.read_config_file()
    
    devicesInConfig = convertDic2NetworkDevicesData(devicesknownDic)
    logging.info(f'device in config file: {len(devicesInConfig)}')

    localIP = scapy.get_if_addr(scapy.conf.iface)
    logging.info(f'localIP = {localIP}')
    
    #get devices on network
    devicesNetworkInfo = list()
    ARPpkt = scapy.Ether(dst='ff:ff:ff:ff:ff')/scapy.ARP(op=1,pdst=f'{localIP}/24')
    received = scapy.srp(ARPpkt,timeout=2,iface=scapy.conf.iface)
    
    for i in range(len(received[0])):
        deviceOnNetwork = NetworkDevicesData(mac = received[0][i].answer.hwsrc, ip = received[0][i].answer.psrc, alias='UNKNOWN')
        devicesNetworkInfo.append(deviceOnNetwork)
            
    logging.info(f'device found on network: {len(devicesNetworkInfo)}')
    #compare devices on config file with devices on the network
    devicesUnknown = list()
    for deviceNK in devicesNetworkInfo:
        for deviceConfig in devicesInConfig:
            if deviceNK.mac == deviceConfig.mac:
                logging.info(f'device found : {deviceNK.mac}')

if __name__ == "__main__":
    main()