import os
import subprocess

def execute(self, inputs, outputs, gvm):
    self.logger.info("Loading pc match config")
    nodeName = inputs['nodeName']
    configFileName = inputs['configFileName']
    
    configPath = os.path.expanduser("~/catkin_ws/src/rtlions/pcmatch/cfg/{}".format(configFileName)) # for pc match
    callArguments = ['rosparam','load', configPath, nodeName]
    self.logger.info(callArguments)
    try:
        outputData = subprocess.check_output(callArguments)
    except Exception as e:
        self.logger.warning(e)
        configPath = os.path.expanduser("~/catkin_ws/src/pcmatch/cfg/{}".format(configFileName)) # for pc match
        callArguments = ['rosparam','load', configPath, nodeName]        
        outputData = subprocess.check_output(callArguments)
    
    self.logger.info("Done")
    
    return 0
