import whereisthis_dict

class location:
    def __init__(self):
        self.rooms = {'shoe': 'office',
             'safe': 'office',
             'coat': 'office',
             'desk': 'office',
             'trash': 'living room',  # trash bin living room
             'sideboard': 'living room',
             'display': 'living room',  # display cabinet
             'coffee': 'living room',
             'couch': 'living room',
             'armchair': 'living room',
             'tv': 'living room',
             'plant': 'living room',
             'living': 'living room',
             'bedroom': 'bedroom', 
             'side': 'bedroom',  # side table
             'bed': 'bedroom',
             'shelf': 'bedroom',
             'sink': 'kitchen',
             'dishwasher': 'kitchen',
             'fridge': 'kitchen',
             'island': 'kitchen',
             'kitchen': 'kitchen',
             'cabinet': 'kitchen',  # kitchen cabinet
             'bin': 'kitchen'
             }

        self.route_gus = ['you are now in the ',
                          'bedroom',
                          'pass the bedroom chest on your left side',
                          'go through the door to the office',
                          'you are now in the ',
                          'office',
                          'in the office turn left',
                          'go through the door to the living room',
                          'pass the trash bin on the left side',
                          'you are now in the ',
                          'living room',
                          'in the living room turn left',
                          'pass the sideboard with drinks on the left side',
                          'go through the hallway to the kitchen',
                          'you are now in the ',
                          'kitchen']

        self.route_ius = ['you are now in the ',
                          'kitchen',
                          'go through the hallway to the living room',
                          'pass the sideboard with drinks on the right side',
                          'you are now in the ',
                          'living room',
                          'in the living room turn right',
                          'pass the trash bin on the right side',
                          'go through the door to the office',
                          'you are now in the ',
                          'office',
                          'in the office turn right',
                          'go through the door to the bedroom',
                          'pass the bedroom chest on your right side',
                          'you are now in the ',
                          'bedroom'
                          ]
        self.names = whereisthis_dict.keyword2Name
        self.waypoints = whereisthis_dict.moveToWp


    def find_path(self, infopoint, target):
        #r_info = self.rooms[infopoint]

        for key, value in self.waypoints.items():
            if infopoint == value:
                r_info = key

        r_info = self.rooms[r_info]

        for key, value in self.waypoints.items():
            if target == value:
                l_target = key
        r_target = self.rooms[l_target]
        

        #r_target = self.waypoints[target]
        start = 0
        text = ""
        route = ""
        for item in self.route_gus:
            if start == 2:
                text += item + ', \n'
                if item == r_target:
                    route = text
                    start = 3
                    break
            if start == 1:
                if r_info not in ['living room', 'office']:
                    text += item + ', \n'
                start = 2

            if item == r_info:
                start = 1
                text += item + ', \n'

        if start < 3:
            text = ""
            start = 0
            for item in self.route_ius:
                if start == 2:
                    text += item + ', \n'
                    if item == r_target:
                        route = text
                        start = 3
                        break
                if start == 1:
                    if r_info not in ['living room', 'office']:
                        text += item + ', \n'
                    start = 2

                if item == r_info:
                    start = 1
                    text += item + ', \n'
        if route == "":
            route = r_info + ', \n'
        
        if l_target in self.names:
            l_target = self.names[l_target]

        return "Go to the center of the " + route + "Finally, go to the " + l_target


if __name__ == '__main__':

    loc = location()
    print(loc.find_path(28, 21))
