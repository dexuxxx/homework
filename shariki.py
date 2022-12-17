from collections import deque
import numpy as np
import argparse
import cv2
import random
 
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())

balls = {}

lower = {'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119)} 
upper = {'green':(86,255,255), 'blue':(117,255,255), 'yellow':(54,255,255)}
colors = {'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217)}

random_colors = ["green", "blue", "yellow"]

def listCompare(list1, list2):
    is_equal = []
    for i in range(0,len(list1)):
        if list1[i] == list2[i]:
            is_equal.append(1)
        else:
            is_equal.append(0)           
    if np.mean(is_equal) == 1:
        return True
    else:
        return False

 
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])
while True:
    (grabbed, frame) = camera.read()
    if args.get("video") and not grabbed:
        break
    
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    for key, value in upper.items():
        kernel = np.ones((9,9),np.uint8)
        mask = cv2.inRange(hsv, lower[key], upper[key])
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            sorted_Colors = sorted(balls, key=balls.get)
            if len(sorted_Colors) == 3:
                cv2.putText(frame, f"Your sequence = {sorted_Colors[0]} {sorted_Colors[1]} {sorted_Colors[2]}", (10,60), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0))
                if listCompare(sorted_Colors, random_colors):           
                    cv2.putText(frame, f"Sequences are equal", (10,80), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0))
        
            if radius > 20:
                cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                cv2.putText(frame,key + " ball", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
 
    cv2.putText(frame, f"Sequence = {random_colors[0]} {random_colors[1]} {random_colors[2]}", (0,30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (245,40,145))
    cv2.imshow("Frame", frame)
    

    #print('green', 'blue', 'yellow' in balls)  

    key = cv2.waitKey(50)
    if key == ord('s'):
        random.shuffle(random_colors)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
 
camera.release()
cv2.destroyAllWindows()