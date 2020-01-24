
def execute(self, inputs, outputs, gvm):
    
    self.logger.info("Evaluating now...")
    
    maxTry = inputs['maxTry']
    triedSoFar = inputs['triedSoFar']
    
    triedSoFar += 1 # if it reaches this state machine, there has been done one try
    
    if triedSoFar >= maxTry:
        self.logger.info("Maxium try's of {} reached! aborting now...".format(maxTry))
        return "abort"
    
    else:
        trysLeft = maxTry - triedSoFar    
        
        infoStr = "Tried {triedSoFar} so far. {trysLeft} try's left!".format(triedSoFar = triedSoFar, trysLeft = trysLeft)
        
        self.logger.info(infoStr)
    
        outputs['triedSoFar'] = triedSoFar 
    
        return "continue"