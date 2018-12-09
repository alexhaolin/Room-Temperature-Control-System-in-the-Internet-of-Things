'''
Created on 2018年9月22日

@author: okok_no
'''

import configparser
import os

DEFAULT_CONFIG_FILE = '/Users/okok_no/Desktop/iot-device/data/ConnectedDevicesConfig.props'

class ConfigUtil:
    configFile = DEFAULT_CONFIG_FILE
    configData = configparser.ConfigParser()
    isLoaded = False
    
    def __init__(self, configFile = None):
        if (configFile != None):
            self.configFile = configFile
        
    def loadConfig(self):
        if (os.path.exists(self.configFile)):
            return self.configData.read(self.configFile)
            self.isLoaded = True
    def getConfig(self, forceReload = False):
        if (self.isLoaded == False or forceReload):
            self.loadConfig()
        return self.configData

    def getConfigFile(self):
        return self.configFile

    def getProperty(self, section, key, forceReload = False):
        return self.getConfig(forceReload).get(section, key)
        
    def isConfigDataLoaded(self):
        return self.isLoaded
        