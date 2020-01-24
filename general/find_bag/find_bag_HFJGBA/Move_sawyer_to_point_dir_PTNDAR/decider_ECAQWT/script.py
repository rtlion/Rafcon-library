from random import randint

def execute(self, inputs, outputs, gvm):
    
    pointDir = str(inputs['pointDirection']).lower()
    currentTry = inputs['currentTry']
    maxTry = inputs['maxTry']
    
    if pointDir == 'right':
        return "right"
    
    elif pointDir == 'left':
        return "left"
    
    else:
        self.logger.info('Found nothing, try again')
        currentTry += 1
        
        if currentTry >= maxTry:
            self.logger.info("Found no direction, going to random pos")
        
            if randint(0, 1) == 0:
                return "right"
            else:
                return "left"
        
        else:
            outputs['currentTry'] = currentTry
            
            return "none"
        