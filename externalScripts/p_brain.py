import socket
import time

'''
    Autor:  MD, 2019
    
    usage: 
    import p_brain
    ef = p_brain.emofani("192.168.43.64", 11005, "192.168.43.231", 11000)
    ef.speaking (True) or (False)
    ef.set_idle (True) or (False)
    ef.talking (True) or (False)
    ef.set_emotion(emote, value) 
        # emote = neutral, sad, attentive, excited, relaxed, sleepy, frustrated - value
        # value = 0 - 100 (default: 100)
    ef.set(emote, value) 
        # emote = pleasure, arousal
        # value = -100 - 100 (not sure, just my guess)
'''

class emofani:
    def __init__(self, source_ip, source_port, target_ip, target_port):
        self.source_ip = source_ip
        self.source_port = source_port
        self.target_ip = target_ip
        self.target_port = target_port
        self.sock = None
        try:
            self.sock = socket.socket(socket.AF_INET,  # Internet
                                 socket.SOCK_DGRAM)  # UDP
            self.sock.bind((source_ip, source_port))
        except:
	    raise Exception("IP/Port not available")

    def set_emotion(self, emote, percent=100):
        self.set("expression", (str(emote)+"%"+str(percent)))

    def set_blush(self, percent):
        now = (int(time.time() * 1000))
        emotion = str("t:" + str(now) + ";s:" + self.source_ip + ";p:" + str(
            self.source_port) + ";d:blush=" + str(percent))
        self.sock.sendto(emotion, (self.target_ip, self.target_port))

    def speaking(self, bool):
        value = "True" if bool else "False"
        self.set("talking", value)

    def set_idle(self, bool):
        value = "True" if bool else "False"
        self.set("idle", value)

    def gaze(self, x, y, z=100):
        self.set("gazex", x)
        self.set("gazey", y)
        self.set("gazez", z)

    def set(self, emote, value):
        now = (int(time.time() * 1000))
        emotion = str("t:" + str(now) + ";s:" + self.source_ip + ";p:" + str(
            self.source_port) + ";d:"+str(emote)+"=" + str(value))
        self.sock.sendto(emotion, (self.target_ip, self.target_port))

    def roll_eyes(self):
        self.set("gazez", -10)
        time.sleep(1)
        self.set("gazez", -5)
        time.sleep(1)
        self.set("gazez", 5)
        time.sleep(1)
        self.set("gazez", 100)


#if __name__ == "__main__":
#    ef = emofani("192.168.43.142", 11005, "192.168.43.231", 11000)
#    ef.speaking(True)
#    ef.set_emotion("happy", 80)
