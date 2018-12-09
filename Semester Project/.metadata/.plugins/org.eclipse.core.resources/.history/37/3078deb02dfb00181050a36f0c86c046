import configparser
import os

Default_CONFIG_FILE = '/home/pi/workspace/iot-device/Lab1/iot-device/data/ConnectedDevicesConfig.props'

class ConfigUtil():
    configfile = Default_CONFIG_FILE
    configdata = configparser.ConfigParser()
    isLoaded   = False
    
    def __init__(self, cf):
        if(cf != None):
            self.configfile = cf
    
    def loadConfig(self):
        if(os.path.exists(self.configfile)):
            self.configdata.read(self.configfile)
            self.isLoaded = True
    
    def getConfig(self, forceReload = False):
        if(self.isLoaded == False or forceReload):
            self.loadConfig()
        return self.configdata
    
    def getConfigFile(self):
        return self.configfile

    def getProperty(self,section, key, forceReload = False):
        return self.getConfig(forceReload).get(section, key)
    
    def isConfigDataLoaded(self):
        return self.isLoaded

