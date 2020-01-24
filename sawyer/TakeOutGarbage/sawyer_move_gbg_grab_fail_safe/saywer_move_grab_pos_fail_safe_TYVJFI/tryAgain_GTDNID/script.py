
def execute(self, inputs, outputs, gvm):
    
    maxTry = inputs['maxTry']
    triedSoFar = inputs['triedSoFar']
    
    if triedSoFar >= maxTry:
        self.logger.info("Reached maxium try's to move the saywer home")
        return 0 # fail

    else:         
        self.logger.info("Try again to move sawyer to home position")
        return 1 # success
