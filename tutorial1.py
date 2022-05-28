import cv2
import random
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    width = int(cam.get(3))
    height = int(cam.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([30,70,70])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    '''image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame'''
    
    
    cv2.imshow('Frame', result)
    cv2.imshow('Mask', mask)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release
cv2.destroyAllWindows()


