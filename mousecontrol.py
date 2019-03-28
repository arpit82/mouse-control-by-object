import numpy as np
import cv2
from pynput.mouse import Button,Controller
v=cv2.VideoCapture(0)
while(1):
    r,i=v.read()
    j=i[:,:,1]
    k=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    p=cv2.subtract(j,k)
    g=cv2.multiply(p,3)
    ret,gth = cv2.threshold(g,35,255,0)
    kernel = np.ones((10,10), np.uint8)
    img_dilation = cv2.dilate(gth, kernel, iterations=1)
    #cv2.imshow('image_sub',p)
    cv2.imshow('image_multiply',g)
    cv2.imshow('image2',gth)
    cv2.imshow('image3',img_dilation)

    image, contours, hierarchy = cv2.findContours(gth,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    ran=len(contours)
    cnt=[contours[i] for i in range(ran)]
    ar=[cv2.contourArea(cnt[i]) for i in range(len(cnt))]
    co=0
    for p in range(len(ar)):
        if ar[p]>1800:
            co+=1
            cnt1= contours[p]
            M = cv2.moments(cnt1)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            print(cx)
            print(cy)

            mouse=Controller()
            mouse.position=(cx,cy)
            mouse.press(Button.left)
            mouse.release(Button.left)
        print(co)

    
 
    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
v.release()
del v

