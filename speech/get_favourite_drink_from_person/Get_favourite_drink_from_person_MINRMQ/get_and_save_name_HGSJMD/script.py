
def execute(self, inputs, outputs, gvm):
    
    personsDict = inputs['personsDict']
    
    name = inputs['name']
    drinks = inputs['drinks']
    
    if drinks is None or len(drinks) == 0:
        outputs['personsDict'] = personsDict
        return "noDetection"
    
    # take the first which we understood
    # because this is with high probabilty the name of the asked person
    favouriteDrink = drinks[0]

    if name in personsDict.keys():
        personsDict[name]['drink'] = favouriteDrink
    else:
        self.logger.error("The name '{}' was not found in personsDicts! Although it should be there!\nPersonsDicts: {}".format(name, personsDict))
            
        
    outputs['drink'] = favouriteDrink
    outputs['personsDict'] = personsDict
    outputs['ttsText'] = "Uhh, {} that is some fancy stuff".format(favouriteDrink)
    
    return 'success'