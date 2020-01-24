
import dataset
import math
import os
import rospy

from matplotlib import path


def execute(self, inputs, outputs, gvm):

    area_cor = inputs["room_borders"]
    db = dataset.connect(
        'sqlite:///%s/humans' % rospy.get_param("/databases/root"),
        engine_kwargs={'connect_args': {'check_same_thread': False}}
    )
    
    humans_in_area = []
    rows = db.query("select x,y,z,u,v,distance,name,age,face_id,pose,waving,gender,color_shirt,color_skin,color_head,color_arms,color_pants from humans")
    counter =  0 
    for human in rows:
        counter += 1 
        #print('x:',human['x'],'y:',human['x'],'z:',human['z'],'u:',human['u'],'v:',human['v'],'age:',human['age'],'gender:',human['gender'], 
        #    'color_shirt:',human['color_shirt'],'color_arms:',human['color_arms'],'color_pants:',human['color_pants'],'name:',human['name'])
        if (human['x'] is not None) and (human['y'] is not None):
            human_x = float(human['x'])
            human_y = float(human['y'])
            if (area_cor.contains_points([(human_x,human_y)])):
                self.logger.info('found at least one human in room')
                if human['distance'] is not None:
                    disHuman = float(human['distance'])
                    self.logger.info('human is {} meters away'.format(disHuman))
                    #if disHuman < 2.5:   # if we want human to be closer than threshold
                    #    print('human is in your grasp')
                    #    return 0
                return 0

    return 1

