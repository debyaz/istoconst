import cv2 as cv
import string
import numpy as np

f = open('coordinates.txt', 'w')
def calculate_coordinates(contmatrix):
    f.write('\n----------------------frame----------------------------\n')
    for i in range(0,len(contmatrix[:][:])):
        for k in range(0,len(contmatrix[i][:])):
            t = contmatrix[i][k]
            x = t[0][0]
            y = t[0][1]
            line = '('+str(x)+','+str(y)+',0),'
            
            f.write(line)
            #print('(',x,',',y,',',0,'),')
cv.namedWindow('MRI', cv.WINDOW_NORMAL)
cv.resizeWindow('MRI',512,512)
num:int = 1

directory:string = 'Series-80341/'
file:string = directory + str(num) + '.jpg'
image = cv.imread(file)
#cv.imshow('MRI',image)

for y in range(0,1):
    num = 1
    for x in range(0,90):
    
        file:string = directory + str(num) + '.jpg'
        image = cv.imread(file)
        gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        a, thresh = cv.threshold(gray,75,255,cv.THRESH_BINARY)
        contours, heir = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
        blank = np.zeros(image.shape[:],dtype='uint8')
        cv.drawContours(blank,contours,-1,(0,255,0) )
        #cv.imshow('contour',gray)
        #cv.imshow('vergin',blank)
        #cv.imshow('MRI',thresh)
        calculate_coordinates(contours)
        num += 1
        



f.close()
#cv.waitKey(0)
cv.destroyAllWindows()
