import sys
import os
import yaml
from matplotlib import path

with open(os.path.expanduser("~/.config/rafcon/config.yaml")  , 'r') as stream:
    yamlData = yaml.safe_load(stream)
    rafconLibPath = yamlData['LIBRARY_PATHS']['rtl_rafcon_lib']
    sys.path.insert(1, rafconLibPath)
    
from externalScripts import store_human_attributes

def execute(self, inputs, outputs, gvm):
    
    dbh= gvm.get_variable(inputs["dbh"], per_reference=True)
    
    area_cor = inputs['livingRoomEdges']
    #area_cor = None # WOHER??
    
    currentDbEntries = inputs['databaseEntries']
    
        
    newDbEntries = store_human_attributes.getHumans(dbh, area_cor, currentDbEntries)    
        
    self.logger.info(newDbEntries)
    
    outputs['newDbEntries'] = newDbEntries
    
    return 0
