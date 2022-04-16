from dataclasses import dataclass

@dataclass
class NetworkDevicesData:
    """Class to record all interesting values of the devices in a network"""
    ip:str
    mac:str
    alias:str