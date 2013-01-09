#!/usr/bin/python
# -*- coding: utf-8-*-
from ConfigParser import ConfigParser
import os
import codecs

class Config(object): 
    """Config class holding all data from configuration files."""
    def __init__(self,filename="config.ini"):
        self._config = ConfigParser()
        self.filename=filename
        self.app={}
        self.token={}
        self.message={}
        self.img={}
        self.time={}
        self.load(filename)

    def __parse_settings(self):
        """Parse SETTINGS section of the config file"""
        result=self.load_config(file_name)
        for key,value in self._config.items():
                print " ",option,"=",self.config.get(section,option)

    def load(self, filename):
        """Load configuration file"""
        self._config.read(filename)
        self.app = dict(self._config.items('app'))
        self.token = dict(self._config.items('token'))
        self.message = dict(self._config.items('message'))
        self.img = dict(self._config.items('img'))
        self.time = dict(self._config.items('time'))

    def load_config(self,filename):
        try:  
            if os.path.exists(filename):  
                config.readfp(codecs.open(file_name, "r", "utf-8-sig"))  
                return config  
        except:  
            print file_name," is not exit"  

if __name__=='__main__':
    c=Config()
    print c.app
