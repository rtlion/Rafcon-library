import os
import rospy
import dataset
import uuid
import os

def execute(self, inputs, outputs, gvm):
    self.logger.info("Getting Database Path")

    try:
        database_path = os.path.join(rospy.get_param("/databases/root"), inputs["db name"])
    except KeyError as e:
        self.logger.warning("Can not find root database in ros! {}\nUsing local one...".format(e))
        #database_path = os.path.expanduser('~/tmpfs2019-05-31/humans')
        database_path = os.path.expanduser('~/bin/rtl_rafcon_lib/externalScripts/humans')
    
    self.logger.info("Connecting to database at %s" % database_path)
    dbc = dataset.connect("sqlite:///" + database_path)
    
    self.logger.info("DBC Type: {}".format(type(dbc)))
      # engine_kwargs={'connect_args': {'check_same_thread': False}}
    
    self.logger.info("connected!!! to database at %s" % database_path)
    # https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa/48234567#48234567


    handle = str(uuid.uuid1())
    self.logger.info("putting db cursor in gvm at %r" % handle)
    gvm.set_variable(handle, dbc, per_reference=True)
    outputs["gvm db cursor"] = handle
    return "success"
