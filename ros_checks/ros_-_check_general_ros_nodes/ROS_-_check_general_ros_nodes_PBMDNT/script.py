import rosnode

def execute(self, inputs, outputs, gvm):
    self.logger.info("Checking general ros nodes...")
    
    # check nodes
    nodesToCheck = ['/rosout']
    
    self.logger.verbose("Nodes to check {}".format(nodesToCheck))
    
    nodeList = rosnode.get_node_names()

    nodeNotFound = False

    for nodeToCheck in nodesToCheck:
        if nodeToCheck not in nodeList:
            self.logger.warning("The Node '{}' is not running!".format(nodeToCheck))
            nodeNotFound = True
            
    if nodeNotFound:
        # atleast one node was not found
        self.logger.info("Not all general ros nodes were found!")
    else:
        self.logger.info("All general ros nodes were found!")
        
            
    return "success"