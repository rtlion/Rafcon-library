
def execute(self, inputs, outputs, gvm):
    
    databaseList = inputs['personsDict']
    names = inputs['names']
    target_human = inputs["target_human"]
    
    if names is None or len(names) == 0:
        outputs['personsDict'] = databaseList
        return "noDetection"
    
    target_human_id = target_human["id"]
    
    person = None
    for row in databaseList:
        if row["id"] == target_human_id:
            person = row 
            break
    
    if not person['name']:
        person['name'] = names[0]
    
    # return the first understood name
    # because this is with high probabilty the name of the asked person
    outputs['name'] = names[0]
    outputs['personsDict'] = databaseList
    
    return 'success'