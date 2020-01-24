
def execute(self, inputs, outputs, gvm):
    
    if gvm.variable_exist("test_mode"):
        testMode = gvm.get_variable('test_mode')
        if testMode:
            self.logger.info("Enter Arena in test mode")
            return "testMode"
        else:
            return "continue"
    
    else:
        return "continue"
