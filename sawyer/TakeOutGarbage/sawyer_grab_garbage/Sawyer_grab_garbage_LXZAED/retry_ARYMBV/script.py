
def execute(self, inputs, outputs, gvm):
    
    maxTry = inputs['maxTry']
    triedSoFar = inputs['triedSoFar']
    triedSoFar += 1 # because we start at 0 we have to add directly 1
    
    if triedSoFar >= maxTry:
        self.logger.info("Tried {} times! Aboarting now...")
        return "abort"
    else:
        triesLeft = maxTry - triedSoFar
        self.logger.info("Got no object in Hand! Trying again! {} tries left".format(triesLeft))
        
        outputs['triedSoFar'] = triedSoFar
        
        return "continue"
