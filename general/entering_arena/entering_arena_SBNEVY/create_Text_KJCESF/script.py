
def execute(self, inputs, outputs, gvm):
    
    challenge = inputs['challenge']
    
    
    outputs['text'] = "Hey I'm ready for {}. Are you ready?".format(challenge)
    return 0
