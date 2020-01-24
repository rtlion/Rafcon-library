
def execute(self, inputs, outputs, gvm):
    
    positions = inputs['positions']
    self.logger.info("Available positions: {}".format(positions))
    
    for posArg, tried in positions.items():
        if not tried:
            outputs['calllParam'] = str(posArg)
            outputs['infoText'] = "Move saywer to {}".format(posArg)
            
            # update dict
            positions[str(posArg)] = True # tried now
            self.logger.info("Updated Positions: {}".format(positions))
            outputs['positions'] = positions
            
            return "success"
            
    # tried every position
    return "triedEveyPosition"