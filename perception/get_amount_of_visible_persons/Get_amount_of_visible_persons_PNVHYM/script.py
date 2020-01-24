import rospy
import dataset

def execute(self, inputs, outputs, gvm):
    db = dataset.connect("sqlite:///" + rospy.get_param("/databases/root") + "/")
    table = db['humans']
    outputs['amount'] = table.find(visible=True).count()
    return 0