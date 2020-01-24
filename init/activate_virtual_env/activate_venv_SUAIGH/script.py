from threading import Thread
import subprocess
from subprocess import check_output
import rospy

def rosLaunchThreadFunction(self, cmd):
    self.logger.info("Calling command: {}".format(cmd))

    # call the command - returns the generated output
    output = check_output(cmd)
    
    # print the output to the rafcon console
    self.logger.verbose("Output: {}".format(output))

def execute(self, inputs, outputs, gvm):
    
    # get inputs
    
    
    # create command for subprocess
    cmd = ['source',' /home/rapha/venv/ma_dev/bin/activate']

    #cmd = []

    # append args
    #for arg in args:
    #    cmd.append(arg)
        
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