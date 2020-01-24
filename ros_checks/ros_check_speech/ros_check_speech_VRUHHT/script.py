import rosnode

def execute(self, inputs, outputs, gvm):
    self.logger.info("Checking speech nodes...")
    
    # check nodes
    nodesToCheck = ['/tts',
                    '/stt_google',
                    '/nlp',
                    '/stt_offline']
                    
    self.logger.verbose("Nodes to check {}".format(nodesToCheck))
    
    nodeList = rosnode.get_node_names()

    nodeNotFound = False

    for nodeToCheck in nodesToCheck:
        if nodeToCheck not in nodeList:
            self.logger.warning("The Node '{}' is not running!".format(nodeToCheck))
            nodeNotFound = True
            
    if nodeNotFound:
        # atleast one node was not found
        self.logger.info("Not all speech nodes were found!")
    else:
        self.logger.info("All speech nodes were found!")
        
            
    return "success"