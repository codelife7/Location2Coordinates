import os,sys
from pathlib import Path
from random import seed
from random import randint
from PIL import Image
import numpy as np
import cv2 as cv2

######################################################
def draw_rectangle(event,x,y,flags,param):
    global img,ix,iy,ex,ey,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y   
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),3,0)
        ex,ey = x,y
######################################################

seed(2)
_location = 'logos\\starbucks'
pathlist = Path(_location).glob('**/*.jpg')
outpath = os.path.join(os.getcwd(), _location + '_processed')


if not os.path.exists(outpath):
    os.mkdir( outpath, 0755 )

writepath = 'logo_location.txt'

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
ex,ey = -1,-1

#annot = ','.join([img_name, str(x1), str(y1), str(x2), str(y2), str(cls_idx)])
mode = 'a' if os.path.exists(writepath) else 'w'
with open(writepath, mode) as f:
    print(outpath)
    for path in pathlist:
        path_in_str = str(path.name)
        print(path.name)
        randomName = str(randint(1000, 9999)) + ".jpg"     
        path.rename( outpath + '\\' + randomName )

        img = cv2.imread( outpath + '\\' + randomName)                
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_rectangle)

        while(1):
            cv2.imshow('image', img)
            k = cv2.waitKey(1) & 0xFF
            #SAVE
            if k == ord('s'):
                f.write(randomName + ', ' + str(ix) +', ' + str(iy) + ', ' + str(ex) +', ' + str(ey) + ',\n')
                break
            #CLEAR
            elif k == ord('c'):
                cv2.destroyAllWindows()
                img = cv2.imread( outpath + '\\' + randomName)                
                cv2.namedWindow('image')
                cv2.setMouseCallback('image', draw_rectangle)
            #SKIP IMAGE                
            elif k == 27:
                break
        cv2.destroyAllWindows()        

