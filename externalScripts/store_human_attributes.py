#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import dataset
import time
import os
import math

#from shapely.geometry import Point
#from shapely.geometry.polygon import Polygon

from matplotlib import path
import matplotlib.pyplot as plt
import numpy as np


class human_attributes:
    def __init__(self, db, area_cor, rafcon_human_database):
        #db = dataset.connect("/home/schwarzbart/rtl_rafcon_lib/externalScripts/humans")
        #self.db = dataset.connect('sqlite:///%s' % os.path.expanduser("/home/schwarzbart/rtl_rafcon_lib/externalScripts/humans"))
        self.db = db
        #self.rows = db.query("select x,y,z,u,v,distance,name,age,face_id,pose,waving,gender,color_shirt,color_skin,color_head,color_arms,color_pants from humans")
        
        # self.area_cor = path.Path([(15, 12), (15, 8), (25, 8), (25, 12)])
        self.area_cor = area_cor
        self.humans_in_area =[]
        self.rafcon_human_database = rafcon_human_database

        self.humans_in_area = self.select_human_in_polygon()
        
        """counter = 0
        for human in rows:
            counter += 1 
            #x = float(human['x'])
            #y = float(human['y'])
            print('x:',human['x'],'y:',human['x'],'z:',human['z'],'u:',human['u'],'v:',human['v'],'age:',human['age'],'gender:',human['gender'], 
                'color_shirt:',human['color_shirt'],'color_arms:',human['color_arms'],'color_pants:',human['color_pants'],'name:',human['name'])
            if (human['x'] is not None) and (human['y'] is not None):
                human_x = float(human['x'])
                human_y = float(human['y'])
                if (area_cor.contains_points([ (human_x,human_y)])):

                    self.humans_in_area.append(human)
        print("total human", counter, 'selected humans', len(self.humans_in_area))
        """

    # select human in a polzgon 
    def select_human_in_polygon(self):


        rows = self.db.query("select x,y,z,u,v,distance,name,age,face_id,waving,gender,color_shirt,color_skin,color_head,color_arms,color_pants from humans")
        counter =  0 
        for human in rows:
            counter += 1 
            #x = float(human['x'])
            #y = float(human['y'])
            #print('x:',human['x'],'y:',human['x'],'z:',human['z'],'u:',human['u'],'v:',human['v'],'age:',human['age'],'gender:',human['gender'], 
            #    'color_shirt:',human['color_shirt'],'color_arms:',human['color_arms'],'color_pants:',human['color_pants'],'name:',human['name'])
            if (human['x'] is not None) and (human['y'] is not None):
                human_x = float(human['x'])
                human_y = float(human['y'])
                if (self.area_cor.contains_points([(human_x,human_y)])):
                    if len(self.rafcon_human_database) == 0:
                        self.rafcon_human_database.append(human)
                    dist_from_cur_human = np.zeros(len(self.rafcon_human_database), dtype=np.float) # .astype('float')
                    counter = 0
                    for raf_h in self.rafcon_human_database:
                        dist_from_cur_human[counter] = (math.sqrt(math.pow(float(raf_h['x']) - human_x, 2) +  math.pow(float(raf_h['y']) - human_y, 2)))
                        counter += 1

                    if min(dist_from_cur_human) > 0.2:
                        self.rafcon_human_database.append(human)
                        print('=============>>>>>> added new person in the rafcon database...')
                    else:
                        print('person already exist in the rafcon database...')

        print('{} persons in a polygon selected....'.format(len(self.rafcon_human_database)))
        return self.rafcon_human_database

def getHumans(db,area_cor, rafcon_human_database):
    ha =human_attributes(db, area_cor, rafcon_human_database)
    return ha.rafcon_human_database

# rafcon human database

#list[]


if __name__ == '__main__':

    #db = dataset.connect('sqlite:///%s' % os.path.expanduser("/home/schwarzbart/rtl_rafcon_lib/externalScripts/humans"))
    db = dataset.connect('sqlite:///%s' % os.path.expanduser("/home/facer2vm/toolBoxes/rtlions/externalScripts/humans"))
    area_cor = path.Path([(15, 12), (15, 8), (25, 8), (25, 12)])
    rafcon_human_database = []

    hm_dt = human_attributes(db, area_cor, rafcon_human_database).rafcon_human_database

    hm_dt = human_attributes(db, area_cor, hm_dt).rafcon_human_database
    
    #point = Point(0.5, 0.5)
    #polygon = Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)])
    #print(polygon.contains(point))

    p = path.Path([(1, 0), (0, 1), (-1, 0), (0, -1)]) 
    print(p.contains_points([ (.51,.5)]))




