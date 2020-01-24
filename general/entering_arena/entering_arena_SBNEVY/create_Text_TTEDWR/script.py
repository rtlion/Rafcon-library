
def execute(self, inputs, outputs, gvm):
    
    challenge = inputs['challenge']
    outputs['text']= "Ok let's start with {}".format(challenge)
    
    return 0
