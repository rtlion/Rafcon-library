
def execute(self, inputs, outputs, gvm):
    
    shelfRow = inputs['shelfRow']
    
    shelfRow += 1 # we need to add one because the code of michael starts at 0 but everything else at 1
    
    callParam = "pos_shelf_{shelfRow}".format(shelfRow = shelfRow)
    
    infoText = "Going to the shelf {shelfRow}".format(shelfRow = shelfRow)
    
    outputs['callParam'] = callParam
    outputs['infoText'] = infoText
    
    
    return 0