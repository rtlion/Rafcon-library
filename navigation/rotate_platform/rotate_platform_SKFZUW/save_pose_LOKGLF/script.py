
def execute(self, inputs, outputs, gvm):
    
    oldPose = inputs['poseStamaped']
    outputs['oldPoseStamped'] = oldPose
    return 0