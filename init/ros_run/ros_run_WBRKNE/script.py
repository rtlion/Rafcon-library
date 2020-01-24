from threading import Thread
from subprocess import check_output
import rospy
import rosnode

def rosRunThreadFunction(self, cmd):
    self.logger.info("Calling command: {}".format(cmd))
    
    # call the command - returns the generated output
    output = check_output(cmd)
    
    # print the output to the rafcon console
    self.logger.verbose("Output: {}".format(output))

def nodeIsRunning(self, node_name):
    
    nodeList = rosnode.get_node_names()

    if node_name not in nodeList:
        self.logger.info("Node not found: {}".format(node_name))
        return False
    else:
        self.logger.info("Node '{}' is already running!".format(node_name))
        return True

def execute(self, inputs, outputs, gvm):
    
    # get inputs
    package = inputs['package']
    executable = inputs['executable']
    args = inputs['args']
    node_name = inputs['node_name'] 
    restart_node_if_running = inputs['restart_node_if_running']
    
    if nodeIsRunning(self, node_name):
        if restart_node_if_running == False:
            return "success"
        
        self.logger.info("Restarting {}".format(package))
    
    # create command for subprocess
    # --screen shows all log in the console
    cmd = ['rosrun', package, executable, '--screen']

    # append args
    for arg in args:
        cmd.append(arg)
        
    # create the thread
    thread = Thread(target = rosRunThreadFunction, args = (self, cmd, ))
    
    try:
        thread.start()
        rospy.sleep(1.0)
    except Exception as e:
        self.logger.error(e)
        self.logger.error(e.args) 
        return "aborted"
    
    return "success"