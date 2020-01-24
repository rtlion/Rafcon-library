# semantische waypoints mit zugeordneten kategorien 
categories = {'shoe': '', # shoe rack
              'safe': '',
              'coat': '', # coat hanger
              'desk': 'candies',
              'bin': '',  # trash bin living room
              'sideboard': 'drinks',
              'display': 'container',  # display cabinet
              'coffee': 'snacks', # coffee table
              'couch': '',
              'armchair': '',
              'tv': '',
              'plant': '',
              'bedroom': '', # bedroom chest
              'side': '',  # side table
              'bed': '',
              'shelf': 'food',
              'sink': 'cleaning',
              'dishwasher': '',
              'fridge': '',
              'island': '',
              'kitchen': 'fruits', # kitchen table
              'cabinet': 'cutlery',  # tableware in kitchen cabinet
              'trash': ''  # trash bin kitchen
              }

moveToWp = {
        'living' : 21,
	     'kitchen' : 17,
	     'bedroom' : 1,
	     'plant' : 20,
	     'bin' : 23,
             'sink': 14,
             'dishwasher': 13,
             'fridge': 12,
             'island': 15,
             'table': 17,
             'cabinet': 17,  # kitchen cabinet
             'trash': 23,  # trash bin living room
             'sideboard': 24,
             'display': 18,  # display cabinet
             'coffee': 21,
             'couch': 22,
             'armchair': 20,
             'tv': 19,
             'shoe': 31, # shoe rack
             'safe': 26,
             'coat': 26,
             'desk': 30,
             'side': 27,  # side table
             'bed': 29,
             'shelf': 28,
	     'localization': 5,}

# categories to poses
waypoints = {'gus_bedroom': 1, # gegen Uhrzeigersinn
             'gus_bedroom chest': 2,
             'gus_door to office': 3,
             'gus_office': 4,
             'gus_localization point': 5,  # after busting the door
             'gus_door to living room': 6,
             'gus_trash bin': 7,
             'gus_living room': 8,
             'gus_sideboard': 9,
             'gus_hallway to kitchen': 10,
             'gus_kitchen': 11,
             'sink': 14,
             'dishwasher': 13,
             'fridge': 12,
             'island': 15,
             'kitchen table': 17,
             'kitchen cabinet': 17,  # kitchen cabinet
             'trash': 23,  # trash bin living room
             'sideboard': 24,
             'display cabinet': 18,  # display cabinet
             'coffee table': 21,
			'living room': 21,
             'couch': 22,
             'armchair': 20,
             'tv': 19,
             'shoe rack': 31,
             'safe': 26,
             'coat hanger': 26,
             'desk': 30,
             'side table': 27,  # side table
             'bed': 29,
             'shelf': 28,
             'uzs_kitchen': 32, # im Uhrzeigersinn
             'uzs_hallway to living room': 33,
             'uzs_sideboard': 34,
             'uzs_living room': 35,
             'uzs_trash bin': 36,
             'uzs_office': 37,
             'uzs_bedroom chest': 38,
             'uzs_bedroom': 39
             }

# objects belong to categories
objects = {'biscuit': 'candies',
           'frosty': 'candies', # frosty fruits
           'snakes': 'candies',
           'cloth': 'cleaning',
           'dishwasher': 'cleaning', # dishwasher tab
           'sponge': 'cleaning',
           'bags': 'cleaning', # trash bags
           'beer': 'drinks',
           'milk': 'drinks', # chocolate milk
           'coke': 'drinks',
           'juice': 'drinks',
           'lemonade': 'drinks',
           'tea bag': 'drinks',
           'water': 'drinks',
           'carrot': 'food',
           'cereals': 'food',
           'noodles': 'food',
           'onion': 'food',
           'vegemite': 'food',
           'apple': 'fruits',
           'kiwi': 'fruits',
           'lemon': 'fruits',
           'orange': 'fruits',
           'pear': 'fruits',
           'cheetos': 'snacks',
           'doritos': 'snacks',
           'chicken': 'snacks', # shapes chicken
           'pizza': 'snacks', # shpaes pizza
           'twisties': 'snacks',
           }

keyword2Name = {'shoe' : 'shoe rack',
		'coat' : 'coat hanger',
		'bin' : 'trash bin in living room',
		'display' : 'display cabinet',
		'coffee' : 'coffee table',
		'bedroom' : 'bedroom chest',
		'side' : 'side table',
		'kitchen' : 'kitchen table',
		'cabinet' : 'kitchen cabinet',
		'trash' : 'trash bin in kitchen',
		'frosty' : 'frosty fruits',
		'dishwasher' : 'dishwasher tab',
		'bags' : 'trash bags',
		'milk' : 'chocolate milk',
		'chicken' : 'shapes chicken',
		'pizza' : 'shapes pizza',
        'living': 'living room'
                }
