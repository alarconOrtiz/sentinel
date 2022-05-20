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

def main() -> None:
    logName = f'sentinel{datetime.now().strftime("_%y_%m_%d")}.log'
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    logging.info(f'Init app log {logName}')
    #get file info
    config = ConfigHandler()
    config.setConfigFile("/Users/alarcon/Documents/GitHub/sentinel/sentinel.ini")
    devicesknownDic = config.read_config_file()
    
    devicesInConfig = convertDic2NetworkDevicesData(devicesknownDic)
    logging.info(f'device in config file: {len(devicesInConfig)}')
    
    localIP = scapy.get_if_addr(scapy.conf.iface)
    logging.info(f'localIP = {localIP}')

    #looking for NetworkIP
    networkIP = localIP[:localIP.rfind('.')+1]
    logging.info(f'network IP :{networkIP}0')
    devices = scapy.arping(f'{networkIP}0/24')

    print(devices[0])
            
    logging.info(f'device(s) found on network: {len(devicesNetworkInfo)} device {deviceinNetwork}')
    #compare devices on config file with devices on the network
    devicesUnknown = list()
    for deviceNK in devicesNetworkInfo:
        for deviceConfig in devicesInConfig:
            if deviceNK.mac == deviceConfig.mac:
                logging.info(f'device found : {deviceNK.mac}')

if __name__ == "__main__":
    main()