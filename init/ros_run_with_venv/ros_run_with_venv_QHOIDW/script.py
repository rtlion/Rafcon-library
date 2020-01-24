from threading import Thread
from subprocess import check_output
import rospy

def rosRunThreadFunction(self, cmd):
    self.logger.info("Calling command: {}".format(cmd))
    
    # call the command - returns the generated output
    output = check_output(cmd)
    
    # print the output to the rafcon console
    self.logger.verbose("Output: {}".format(output))

def execute(self, inputs, outputs, gvm):
    
    # get inputs
    package = inputs['package']
    executable = inputs['executable']
    args = inputs['args']
    
    # create command for subprocess
    # --screen shows all log in the console
    
    #cmd = ['rosrun', package, executable, '--screen']
    #cmd = ['source', '/home/leonart/virtualenv/tfpose/bin/activate', '&&', 'rosrun', package, executable, '--screen']

    cmd = ['source', '/home/leonart/virtualenv/tfpose/bin/activate']

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