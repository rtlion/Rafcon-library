import math


# set treshhold for for angle in deg
angleTreshold = 15


class Vector(tuple):
    def __add__(self, a):
        # TODO: check lengths are compatable.
        return Vector(x + y for x, y in zip(self, a))

    def __mul__(self, c):
        return c[0] * self[0] + c[1] * self[1]
        # return Vector(x * c for x in self)

    def __rmul__(self, c):
        return Vector(c * x for x in self)


def chooseBag(bodyparts):
    # Check if human has all of the depending bodyparts: left and right shoulder (2, 5), wrist (4, 7) as well neck (1)
    # calculate human middle axis using neck and hip
    if bodyparts.get(1) and bodyparts.get(8) and bodyparts.get(11):
        # calculate human middle axis using the neck and the middle of both hips
        humanHipMean = Vector(((bodyparts[11].x - bodyparts[8].x)/2 + bodyparts[8].x, (bodyparts[8].y + bodyparts[11].y)/2))
        humanAxisVec = Vector(((bodyparts[1].x - humanHipMean[0]), (bodyparts[1].y - humanHipMean[1])))
        absHumanAxis = math.sqrt(math.pow((bodyparts[1].x - humanHipMean[0]), 2) + math.pow((bodyparts[1].y - humanHipMean[1]), 2))
        print("human Axis: ", humanAxisVec)
        print("human Abs Axis: ", absHumanAxis)
        bodyAxis = True

    # if only neck was found
    elif bodyparts.get(1):
        # calculate human middle axis
        humanAxisVec = Vector(((bodyparts[1].x), (bodyparts[1].y - bodyparts[1].y * 0.5)))
        absHumanAxis = math.sqrt(math.pow(bodyparts[1].x, 2) + math.pow((bodyparts[1].y - bodyparts[1].y * 0.5), 2))
        print("human Axis: ", humanAxisVec)
        print("human Abs Axis: ", absHumanAxis)
        bodyAxis = True
    else:
        bodyAxis = False



    # check if human body axis was calculated
    if bodyAxis:
               ######################### Left side ########################################
        # check if left shoulder and wrist is contained in bodyparts?!
        if bodyparts.get(5) and bodyparts.get(7):
            print("BP5 ", bodyparts.get(5), "BP7 ", bodyparts.get(7))
            # calculate vector for left shoulder and left wrist
            leftArmVec = Vector(((bodyparts[5].x - bodyparts[7].x), (bodyparts[5].y - bodyparts[7].y)))
            print("left Arm Vec: ", leftArmVec)

            # calculate abs for left shoulder and left wrist
            absLeftArm = math.sqrt(
                math.pow((bodyparts[5].x - bodyparts[7].x), 2) + math.pow((bodyparts[5].y - bodyparts[7].y), 2))
            print("left Arm Abs: ", absLeftArm)

            # calculate angle between leftArmVec and humanAxisVec
            leftVecProd = (humanAxisVec.__mul__(leftArmVec))
            print("left Vec Prod: ", leftVecProd)
            try:
                leftAlpha = math.acos((leftVecProd) / float(absHumanAxis * absLeftArm)) * (180 / math.pi)
                print("left Angle: ", leftAlpha)
            except Exception as e:
                print e
                if absLeftArm != 0:
                    if ((leftVecProd) / float(absHumanAxis * absLeftArm)) < 0:
                        leftAlpha = math.acos(-1) * (180 / math.pi)
                        print("left Angle: ", leftAlpha)
                    else:
                        leftAlpha = math.acos(1) * (180 / math.pi)
                        print("left Angle: ", leftAlpha)
                else:
                    leftAlpha = 0.0
                    print("\n\n\n WAR GLEICH \n\n\n")
        else:
            leftAlpha = 0.0
            print("left Angle: ", leftAlpha)


        ######################### right side ########################################
        # check if right shoulder and wrist is contained in bodyparts?!
        if bodyparts.get(2) and bodyparts.get(4):
            print("BP2 ", bodyparts.get(2), "BP4 ", bodyparts.get(4))
            rightArmVec = Vector(((bodyparts[2].x - bodyparts[4].x), (bodyparts[2].y - bodyparts[4].y)))
            print("right Arm Vec: ", rightArmVec)

            # calculate abs for right shoulder and right wrist
            absRightArm = math.sqrt(
                math.pow((bodyparts[2].x - bodyparts[4].x), 2) + math.pow((bodyparts[2].y - bodyparts[4].y), 2))
            print("right Arm Abs: ", absRightArm)

            # calculate angle between rightArmVec and humanAxisVec
            rightVecProd = (humanAxisVec.__mul__(rightArmVec))
            print("right Vec Prod: ", rightVecProd)
            try:
                rightAlpha = math.acos((rightVecProd) / float(absHumanAxis * absRightArm)) * (180 / math.pi)
                print("right Angle: ", rightAlpha)
            except Exception as e:
                print e
                if absRightArm != 0:
                    if (rightVecProd) / float(absHumanAxis * absRightArm) < 0:
                        rightAlpha = math.acos(-1) * (180 / math.pi)
                    else:
                        rightAlpha = math.acos(1) * (180 / math.pi)
                    print("right Angle: ", rightAlpha)
                else:
                    rightAlpha = 0.0
                    print("\n\n\n WAR GLEICH \n\n\n")

        else:
            rightAlpha = 0.0
            print("right Angle: ", rightAlpha)




        if leftAlpha != 0.0 and rightAlpha != 0.0:
            # check if leftAlpha is bigger than rightAlpha and bigger than a default treshold
            if leftAlpha >= angleTreshold and rightAlpha >= angleTreshold:
                side = "Non"

            elif leftAlpha < rightAlpha and rightAlpha >= angleTreshold:
                side = "right"

            elif leftAlpha > rightAlpha and leftAlpha >= angleTreshold:
                side = "left"

            else:
                side = "Non"
        else:
            side = "NOOOOOOOONE"

    # couldnt calculate the human body axis
    else:
        side = "No able to evaluate"

    return side



def biggestPeron(humans):
    humanSize = [0] * len(humans)
    minimum = [1] * len(humans)
    maximum = [0] * len(humans)
    k = 0

    if humans:
        # iterate through all humans found in image
        for human in humans:

            #calculate the minimum and maximum of a person
            #iterate through all bodyparts and search for min and max Y -> Size Person
            for bp in human.body_parts:
                if human.body_parts[bp].y >= maximum[k]:
                    maximum[k] = human.body_parts[bp].y

                if human.body_parts[bp].y <= minimum[k]:
                    minimum[k] = human.body_parts[bp].y

            # calculate the size of the human bonemodel
            humanSize[k] = maximum[k] - minimum[k]
            print ("Size human", humanSize[k])
            k += 1


        # who is the biggest person in this image
        print("liste HumanSize", humanSize)
        if humanSize[0] != 0:
            bigHumanIndex = humanSize.index(max(humanSize))
            #bigHumanIndex = 1
            print("biggest Human Size: ", max(humanSize), " at pos: ", bigHumanIndex)
            return humans[bigHumanIndex]
        else:
            return None

    else:
        return None


