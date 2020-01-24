from threading import Thread
import subprocess
from subprocess import check_output
import rospy
import rosnode

def rosLaunchThreadFunction(self, cmd):
    self.logger.info("Calling command: {}".format(cmd))

    # call the command - returns the generated output
    output = check_output(cmd)
    
    # print the output to the rafcon console
    self.logger.verbose("Output: {}".format(output))

def allNodesAreRunning(self, node_name_list):
    
    nodesMissing = 0
    
    nodeList = rosnode.get_node_names()

    for node_name in node_name_list:
        if node_name not in nodeList:
            self.logger.info("Node not found: {}".format(node_name))
            nodesMissing += 1
        else:
            self.logger.info("Node '{}' is already running!".format(node_name))
        
    
    if nodesMissing > 0:
        # Atleast 1 node is missing
        return False
    else:
        # No node is missing - all running
        return True
        
    
def execute(self, inputs, outputs, gvm):
    
    # get inputs
    package = inputs['package']
    executable = inputs['executable']
    args = inputs['args']
    restart_if_nodes_running = inputs['restart_if_nodes_running']
    node_name_list = inputs['node_name_list']
    
    if allNodesAreRunning(self, node_name_list):
        if restart_if_nodes_running == False:
            return "success"
        
        self.logger.info("Restarting {}".format(package))
    
    # create command for subprocess
    cmd = ['roslaunch', package, executable]

    # append args
    for arg in args:
        cmd.append(arg)
        
    # create the thread
    thread = Thread(target = rosLaunchThreadFunction, args = (self, cmd, ))
    
    try:
        thread.start()
        rospy.sleep(2)
    except Exception as e:
        self.logger.error(e)
        self.logger.error(e.args) 
        return "aborted"
    
    return "success"