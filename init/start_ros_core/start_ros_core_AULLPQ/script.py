from subprocess import check_output
from threading import Thread
import subprocess
import rospy
import socket
import rosgraph

def startRosCoreFunction(self, cmd):
    
    self.logger.info("Trying to start ROS CORE")
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = process.communicate()
    
    self.logger.verbose(out)
    
    if err != None:
        self.logger.error(err)
        
    self.logger.info("Done!")

def startRosCore(self, thread):
    try:
        thread.start()
        rospy.sleep(3)
        return "success"
    except Exception as e:
        self.logger.error(e)
        self.logger.error(e.args) 
        return "aborted"
        
def killRosCore(self):
    
    cmd = ['killall', '-9', 'roscore', '&&', 'killall', '-9', 'rosmaster']

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = process.communicate()
    
    self.logger.verbose(out)
    
    if err != None:
        self.logger.error(err)
        
    rospy.sleep(1.0) # wait a second

def execute(self, inputs, outputs, gvm):
    
    port = inputs['port']
    
    # it's actually just this command
    cmd = ['roscore']
    
    if port != None:
        cmd.append('-p {}'.format(port))
        
    # create the thread
    thread = Thread(target = startRosCoreFunction, args = (self, cmd, ))
    
    try:
        rosgraph.Master('/rostopic').getPid()
    except socket.error:
        #self.logger.warning("Unable to communicate with master!")
        # No ros core running -> start it
        return startRosCore(self, thread)
    
    # ros core active - restart if True
    if inputs['restart_if_running']:
        self.logger.info("ROS CORE already running - killing ROS CORE!")
        killRosCore(self)
    
        self.logger.info("Restarting ROS CORE!")
        return startRosCore(self, thread)
        
    self.logger.info("ROS CORE already running!")
    
    return "success"