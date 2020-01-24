
def execute(self, inputs, outputs, gvm):
    
    waveDetection = inputs['waveDetection']
    
    if waveDetection:
        return "yes"
    else:
        return "no"