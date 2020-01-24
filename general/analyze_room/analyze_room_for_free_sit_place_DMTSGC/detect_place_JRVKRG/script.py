''' 
sofa.append({"x1": 0.8, "y1": 0.1, "x2": 1.2, "y2": 0.3, "free": True, "perspective": 1, "waypoint": 14})
'''
import os
import cPickle as pickle

def execute(self, inputs, outputs, gvm):
    dbh= gvm.get_variable(inputs["dbh"], per_reference=True)
    
    rw=dbh.query("select x,y,z from humans")
    
    chairs = os.path.expanduser(inputs["wpp chairs"])
    self.logger.debug("loading wpp file %r ..." % chairs)
    
    with open(chairs, 'rb') as f: 
        wp_chairs = pickle.load(f)
        #for point in waypoints:
        #print d[point].position.x
        #print d[point].position.y
    self.logger.info("loaded %r pickled waypoints" % len(chairs))
    
    sofas = os.path.expanduser(inputs["wpp sofas"])
    self.logger.debug("loading wpp file %r ..." % sofas)
    
    with open(sofas, 'rb') as f: 
        wp_sofas = pickle.load(f)
        #for point in waypoints:
        #print d[point].position.x
        #print d[point].position.y
    self.logger.info("loaded %r pickled waypoints" % len(sofas))
    
    places = []
    
    for wp in wp_chairs:
        places.append({'wp': wp_chairs[wp], 'type': 'chair', 'free': True})
        self.logger.debug(wp)
    for wp in wp_sofas:
        self.logger.debug(wp)
        places.append({'wp': wp_chairs[wp], 'type': 'sofa', 'free': True})
        
        
    for human in rw:
        self.logger.info(human)
        for place in places:
            try:
                x = float(human['x'])
                y = float(human['y'])
                x1 = place['wp'].position.x
                self.logger.info(x1)
                y1 = place['wp'].position.y
                dist = ((x - x1)**2 + (y-y1)**2)**.5
                self.logger.info(dist)
                if (dist < 2.5):
                    place["free"] = False
                    self.logger.debug("occupied spot on waypoint: " + str(place["wp"]))
            except TypeError:
                self.logger.debug("Human position not detected")
            
    for wp in places:
        if wp["free"] == True:
            #outputs["waypoint"] = str(wp["wp"])
            outputs["pickledWaypoint"] = pickle.dumps(wp["wp"])
            
            self.logger.debug("** free spot on {wpType} at waypoint {wp}".format(wpType=wp['type'], wp=wp['wp']))
            return 0
            
    outputs["waypoint"] = -1
    return "nothingFound"
