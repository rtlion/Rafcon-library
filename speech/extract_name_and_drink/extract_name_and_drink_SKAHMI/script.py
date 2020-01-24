import rospy
import rtl_comm.srv

def execute(self, inputs, outputs, gvm):
    
    # names we can search for
    exampleNames = ["Amelia", "Angel", "Ava", "Charlie", "Charlotte",
    "Mia", "Olivia", "Parker", "Sam",
    "Hunter", "Jack", "Max", "Noah", "Oliver","Thomas",
    "William", "Michael", "Maria", "Kim", "Daniel", "Isabel",
    "Alex", "John", "Barbara", "Kevin", "William", "Emma","Sasha",
    "Christoph", "Susan", "Joey", "Charlie", "Lee", "Bruce", "Toni", "Nicky"]
    
    # drinks we can search for
    exampleDrinks = ["water", "tea","milk", "beer",
    "lemonade", "chocolate", "juice", "whiskey", "coke", 'cloak']
    
    transcript = inputs['transcript']
    #sample = "Hello my Name is John and my favoriture drink is Beer"
    
    self.logger.info("Getting names and drinks from transcript: {}".format(transcript))
    end = rospy.ServiceProxy('nlp/end', rtl_comm.srv.namesAndDrinks)
    data = end(transcript, exampleNames, exampleDrinks)
    
    names = data.names
    drinks = data.drinks
    
    self.logger.info("Names: {}\nDrinks: {}".format(names, drinks))
    
    # remove duplicate
    newNames = []
    newDrinks = []
    
    for name in names:
        if name not in newNames:
            newNames.append(name)
            break
            
    for drink in drinks:
        if drink not in newDrinks:
            newDrinks.append(drink)
            break
    
    
    outputs['names'] = names
    outputs['drinks'] = drinks
    
    return 0

