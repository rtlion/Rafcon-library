
def execute(self, inputs, outputs, gvm):
    
    personsDict = inputs['personsDict']
    names = inputs['names']
    
    if names is None or len(names) == 0:
        outputs['personsDict'] = personsDict
        return "noDetection"
    
    # take the first which we understood
    # because this is with high probabilty the name of the asked person
    name = names[0]

    if name not in personsDict.keys():
        personsDict[name] = {'name' : name}
    else:
        self.logger.warning("The name '{}' is already in the personsDict! It will be overwritten".format(name))
        personsDict[name] = {'name' : name}
            
        
    outputs['name'] = name
    outputs['personsDict'] = personsDict
    outputs['ttsText'] = "Nice to meet you {}".format(name)
    
    return 'success'