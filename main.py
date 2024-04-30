import cv2 as cv
import string

cv.namedWindow('MRI', cv.WINDOW_NORMAL)
cv.resizeWindow('MRI',512,512)
num:int = 1

directory:string = 'Series-80341/'
file:string = directory + str(num) + '.jpg'
image = cv.imread(file)
cv.imshow('MRI',image)

for x in range(0,90):
    
    file:string = directory + str(num) + '.jpg'
    image = cv.imread(file)
    cv.imshow('MRI',image)
    num += 1
    cv.waitKey(10)


cv.waitKey(0)
cv.destroyAllWindows()
