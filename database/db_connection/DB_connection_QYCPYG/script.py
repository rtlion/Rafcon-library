import rospy
import dataset

"""
Instructions:

Customize the section 'Asking the DB' to your liking.
For Example change the name='sht' to age=1.5 or id=your_variable

Important:
All of the found fields will be available as outputs with the
same name as the fields in the Database.

"""

def execute(self, inputs, outputs, gvm):
    # Connecting to Database
    self.logger.info("Getting Database Path")
    database_path = 'sqlite:///%shumans' % rospy.get_param("/databases/root")
    self.logger.info("Connecting to database at %s" % database_path)
    db = dataset.connect(database_path)
    table = db['humans']
    
    # Asking the DB (Customize this line)
    db_answer = table.find_one(name='John')
    
    # Handle no Information
    if not db_answer:
        self.logger.warn("Could not retrieve information")
        return "no_information"
    self.logger.info("Information: %s" % str(db_answer))
    
    # Put the Information in the corresponding output fields
    for key in db_answer.keys():
        if not db_answer.get(key): continue
        data = db_answer.get(key)
        if isinstance(data, unicode):
            data = str(data)
        outputs[key] = data
    return "success"
