# USAGE
# python yolo_video.py --input videos/airport.mp4 --output output/airport_output.avi --yolo yolo-coco

# import the necessary packages edited 2019.05.14
#from imutils.video import VideoStream
#from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import os


class rack:


    def __init__(self, video=False):

        self.shelf = 0
        self.H = 0
        self.W = 0
        self.video = video

        labelsPath = "/home/leonart/brain/darknet/data/sydney.names"
        # load the COCO class labels our YOLO model was trained on
        # derive the paths to the YOLO weights and model configuration
        weightsPath = "/home/leonart/brain/darknet/sydney_5300.weights"
        configPath = "/home/leonart/brain/darknet/cfg/sydney2019.cfg"

        self.LABELS = open(labelsPath).read().strip().split("\n")


        # initialize a list of colors to represent each possible class label
        np.random.seed(42)
        self.COLORS = np.random.randint(0, 255, size=(len(self.LABELS), 3),
                                   dtype="uint8")
        self.contentDict = {}

        self.net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
        self.ln = self.net.getLayerNames()
        self.ln = [self.ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        # load our YOLO object detector trained on COCO dataset (80 classes)
        # and determine only the *output* layer names that we need from YOLO
        # print("[INFO] loading YOLO from disk...")

    def detect(self, frame, conf=0.4, thrsh=0.4):

        frame = imutils.resize(frame, width=700)
        # if the frame dimensions are empty, grab them
        # if W is None or H is None:
        (self.H, self.W) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                     swapRB=True, crop=False)
        self.net.setInput(blob)
        start = time.time()
        layerOutputs = self.net.forward(self.ln)
        end = time.time()

        # initialize our lists of detected bounding boxes, confidences,
        # and class IDs, respectively
        boxes = []
        confidences = []
        classIDs = []

        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability)
                # of the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence > conf:
                    # scale the bounding box coordinates back relative to
                    # the size of the image, keeping in mind that YOLO
                    # actually returns the center (x, y)-coordinates of
                    # the bounding box followed by the boxes' width and
                    # height
                    box = detection[0:4] * np.array([self.W, self.H, self.W, self.H])
                    (centerX, centerY, width, height) = box.astype("int")

                    # use the center (x, y)-coordinates to derive the top
                    # and and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # update our list of bounding box coordinates,
                    # confidences, and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        # apply non-maxima suppression to suppress weak, overlapping
        # bounding boxes
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, conf, thrsh)
        return idxs, boxes, confidences, classIDs

    def process_shelf(self, frame, shelf=1, conf=0.4, thrsh=0.4):

        idxs, boxes, confidences, classIDs = self.detect(frame, conf, thrsh)

        items = []

	cat = None

        # ensure at least one detection exists
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                # extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                try:
                    lab, cat, greifbarkeit = str.split(self.LABELS[classIDs[i]], '.')
                except:
                    lab = self.LABELS[classIDs[i]]
                    cat = self.LABELS[classIDs[i]]

                if y < self.H*2/3 and y + h > self.H/3:
                    items.append({'label': lab, 'category': cat, 'x': x, 'y': y, 'w': w, 'h': h, 'row': shelf})

                    if self.video:
                        # draw a bounding box rectangle and label on the frame
                        color = [int(c) for c in self.COLORS[classIDs[i]]]
                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                        text = "{}: {:.4f}".format(self.LABELS[classIDs[i]],
                                                   confidences[i])
                        cv2.putText(frame, text, (x, y - 5),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                        # print(text + ' x = ' + str(x) + ' y = ' + str(y))

        #dictionary = dict()

        #category = "nichts"

        for d in items:
            self.contentDict[str(d["row"])] = str(d["category"])
            #category = str(d["category"])

        #for d in items:
        #    dictionary[str(d['row'])] = str(d['category'])

        #with open('categories.txt', 'a') as file:
        #    for i, c in dictionary.items():
        #        file.writelines(str(i) + ' ' + str(c) + '\n')

        return len(idxs), cat

    def process_table(self, frame, categories="", conf=0.4, thrsh=0.4):

        idxs, boxes, confidences, classIDs = self.detect(frame, conf, thrsh)
        table = []
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                # extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                try:
                    lab, cat, greif = str.split(self.LABELS[classIDs[i]], '.')
                except:
                    lab = self.LABELS[classIDs[i]]
                    cat = self.LABELS[classIDs[i]]
                    greif = 1

                table.append({'label': lab, 'category': cat, 'greifbarkeit': greif, 'x': x, 'y': y, 'w': w, 'h': h, 'shelf': 0})

                if self.video:
                    # draw a bounding box rectangle and label on the frame
                    color = [int(c) for c in self.COLORS[classIDs[i]]]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    text = "{}: {:.4f}".format(self.LABELS[classIDs[i]],
                                               confidences[i])
                    cv2.putText(frame, text, (x, y - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    #print(text + ' x = ' + str(x) + ' y = ' + str(y))

        if self.video:
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

        items = []

        #categories = dict()
        #with open('categories.txt', 'r') as file:
        #    for line in file:
         #       line = line.strip()
         #       categories[line.split(' ')[0]] = line.split(' ')[1]



        # nach Greifbarkeit sortieren
        table = sorted(table, key=lambda k: k['greifbarkeit'])

        objInCat = []

        # nach categories aussortieren
        if categories is not None:
            
            for d in table:
                nr = 1
                for item in categories:
                    if item == str(cat):
                        d['shelf'] = nr
                        objInCat.append(d)
                        break
                    nr+=1

            #for shelf, c in self.contentDict.items():
            #    if str(d['category']) == str(c):
            #        d['shelf'] = shelf
            #        objInCat.append(d)
            #        #print(str(d['label']) + ' gehoert in row ' + str(i))

        # if there are objects with shelf filter others out
        # otherwise send all objects
        if len(objInCat) > 0:
            table = objInCat

        return_table = []
        i=0
        for d in table:
            return_table.append(d)
            i += 1
            if i > 2:
                break

        # todo: sort for distance
        for o in objInCat:
            print(o)

        return return_table

    def clear(self):
        #f = open('categories.txt', 'w')
        #f.write("")
        #f.close()
        self.contentDict = {}

    def get_category(self, shelfNr):
        for item in self.contentDict:
            if item["shelf"] == shelfNr:
                return item["category"]
        return ""


if __name__ == '__main__':
    # initialize the video stream, pointer to output video file, and
    # frame dimensions
    vs = cv2.VideoCapture()

    print("[INFO] starting video stream...")
    #vs = VideoStream(src=0).start()
    time.sleep(1.0)

    regal = rack(True)
    '''
    shelf = np.zeros(4)

    while shelf[0] == 0:
        shelf[0] = regal.process_shelf(vs.frame, 1)

    while shelf[1] == 0:
        shelf[1] = regal.process_shelf(vs.frame, 2)

    while shelf[2] == 0:
        shelf[2] = regal.process_shelf(vs.frame, 3)

    while shelf[3] == 0:
        shelf[3] = regal.process_shelf(vs.frame, 4)

    while True:
        result = regal.process_table(vs.frame)
        print(result)
'''
    regal.clear()

    image = cv2.imread('/home/rapha/bin/sg/testBild.jpg')

    regal = rack()
    categories = []
    shelf = 0

    while shelf == 0:
        shelf, category = regal.process_shelf(image, 1)
        print("trying to detect objects")

    categories.append(category)

    result = regal.process_shelf(image, categories)

    print(category)
