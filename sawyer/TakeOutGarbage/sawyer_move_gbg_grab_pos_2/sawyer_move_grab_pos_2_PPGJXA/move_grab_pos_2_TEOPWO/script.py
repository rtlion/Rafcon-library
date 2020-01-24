import subprocess

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    if testMode:
        import time
        time.sleep(0.5)
        self.logger.info("Saywer move grab position 2!")
        return 1 # success
    else:
    
        callArguments = ['rosservice','call','/sawyer_move', 'pos2']
        outputData = subprocess.check_output(callArguments)

        self.logger.info(outputData)
        
        if outputData == 1: # success
            return 1
        else:
            return 0 # fail
