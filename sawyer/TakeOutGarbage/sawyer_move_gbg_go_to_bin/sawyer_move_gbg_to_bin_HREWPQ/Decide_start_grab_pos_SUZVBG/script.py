
def execute(self, inputs, outputs, gvm):
    
    lastGrabPos = inputs['lastGrabPos']
    
    if lastGrabPos is None:
        return "gotoPos1"
        
    elif lastGrabPos == 1:
        return "gotoPos2"
        
    elif lastGrabPos == 2:
        return "gotoPos1"
        
    else:
        return "gotoPos1"
