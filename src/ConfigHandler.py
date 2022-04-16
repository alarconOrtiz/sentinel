import configparser

class ConfigHandler:
    def __init__(self) -> None:
        self.fileConfig = None

    def setConfigFile(self, filePath : str) -> None:
        self.fileConfig = filePath

    def read_config_file(self) -> dict:
        knownDevices = dict()
        config = configparser.ConfigParser()
        config.read(self.fileConfig)
        #read all devices in config file
        index_device = 1
        next_device = True
        while next_device : 
            try:
                macDevice = config.get('DevicesKnown','mac{}'.format(index_device))
                knownDevices['mac{}'.format(index_device)] = [macDevice,'ip','alias']
                index_device = index_device + 1
            except Exception as e:
                if(type(e) == configparser.NoOptionError ):
                    next_device = False
                else:
                    raise e
        return knownDevices