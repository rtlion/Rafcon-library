
def execute(self, inputs, outputs, gvm):
    
    shelfRow = inputs['shelfRow']
    
    label = inputs['label']
    
    if label is None:
        label = "Object"
    
    if shelfRow == 0:
        # don't no where to put make random row
        import random
        shelfRow = random.randint(1,4)
        self.logger.info("Shelf row was 0! Put on a random shelf...")
    
    
    callParam = "traj_shelf_place_{shelfRow}".format(shelfRow = shelfRow)
    
    infoText = "Place {objectLabel} into shelf row {shelfRow}".format(objectLabel = label, shelfRow = shelfRow)
    
    outputs['callParam'] = callParam
    outputs['infoText'] = infoText
    
    return 0