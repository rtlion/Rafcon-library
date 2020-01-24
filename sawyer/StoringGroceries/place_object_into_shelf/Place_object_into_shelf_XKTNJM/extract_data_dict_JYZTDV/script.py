
def execute(self, inputs, outputs, gvm):
    self.logger.debug("extracting data dict")
    
    dataDict = inputs['dataDict']
    
    if dataDict is None:
        self.logger.warning("Data dict is None!")
    
    try:
        label = dataDict['label']
        shelfRow = dataDict['shelfRow']
    
    except KeyError as e:
        self.logger.warning("Data dict has no {}\nData dict: {}".format(e, dataDict))
    
    return 0
