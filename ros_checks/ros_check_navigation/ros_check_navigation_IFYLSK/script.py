import rosnode

def execute(self, inputs, outputs, gvm):
    self.logger.info("Checking navigation nodes...")
    
    # check nodes
    nodesToCheck = ['/move_base',
                    '/amcl']
                    
    self.logger.verbose("Nodes to check {}".format(nodesToCheck))
    
    nodeList = rosnode.get_node_names()

    nodeNotFound = False

    for nodeToCheck in nodesToCheck:
        if nodeToCheck not in nodeList:
            self.logger.warning("The Node '{}' is not running!".format(nodeToCheck))
            nodeNotFound = True
            
    if nodeNotFound:
        # atleast one node was not found
        self.logger.info("Not all navigation nodes were found!")
    else:
        self.logger.info("All navigation nodes were found!")
        
            
    return "success"