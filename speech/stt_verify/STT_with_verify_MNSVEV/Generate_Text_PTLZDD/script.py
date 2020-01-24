
def execute(self, inputs, outputs, gvm):
    transcript = inputs['transcript']
    outputs['text'] = "I understood %s is that right?" % transcript
    return 0
