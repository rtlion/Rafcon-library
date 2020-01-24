
def execute(self, inputs, outputs, gvm):
    
    dataDict = inputs['dataDict']
    
    objLabel = dataDict['label']
    
    textStr = "Going to the {label}".format(label = objLabel)
    
    outputs['textStr'] = textStr
    
    
    return 0
