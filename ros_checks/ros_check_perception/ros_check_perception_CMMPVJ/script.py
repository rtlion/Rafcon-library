import rosnode

def execute(self, inputs, outputs, gvm):
    self.logger.info("Checking perception nodes...")
    
    # check nodes
    nodesToCheck = ['/camera/realsense2_camera_manager',
                    '/realsense_tf',
                    '/camera/realsense2_camera',
                    '/followMe']
                    
    self.logger.verbose("Nodes to check {}".format(nodesToCheck))
    
    nodeList = rosnode.get_node_names()

    nodeNotFound = False

    for nodeToCheck in nodesToCheck:
        if nodeToCheck not in nodeList:
            self.logger.warning("The Node '{}' is not running!".format(nodeToCheck))
            nodeNotFound = True
            
    if nodeNotFound:
        # atleast one node was not found
        self.logger.info("Not all perception nodes were found!")
    else:
        self.logger.info("All perception nodes were found!")
        
            
    return "success"