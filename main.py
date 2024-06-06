import cv2 as cv
import string
import numpy as np
import bpy

#f = open('coordinates.txt', 'w')
def calculate_coordinates(contmatrix, layer:float):
    verts = []
    for i in range(0,len(contmatrix[:][:])):
        for k in range(0,len(contmatrix[i][:])):
            t = contmatrix[i][k]
            #x = t[0][0]
            #y = t[0][1]
            coordinates = (t[0][0],t[0][1],layer)
            verts.append(coordinates)

    return verts
cv.namedWindow('MRI', cv.WINDOW_NORMAL)
cv.resizeWindow('MRI',512,512)
num:int = 1

directory:string = 'Series-80341/'
file:string = directory + str(num) + '.jpg'
image = cv.imread(file)
#cv.imshow('MRI',image)
offsetValue:float = 5
for y in range(0,1):
    num = 1
    for x in range(0,90):
    
        file:string = directory + str(num) + '.jpg'
        image = cv.imread(file)
        gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        a, thresh = cv.threshold(gray,75,255,cv.THRESH_BINARY)
        contours, heir = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
        blank = np.zeros(image.shape[:],dtype='uint8')
        #cv.drawContours(blank,contours,-1,(0,255,0) )
        #cv.imshow('contour',gray)
        #cv.imshow('vergin',blank)
        #cv.imshow('MRI',thresh)
        
        #blender open
        vertex = calculate_coordinates(contours,num*offsetValue)
        faces = []
        edges = []
        mesh_data = bpy.data.meshes.new("cube_data")
        mesh_data.from_pydata(vertex, edges, faces)
        mesh_obj = bpy.data.objects.new("cube_object", mesh_data)
        bpy.context.collection.objects.link(mesh_obj)
        #blender close
        num += 1
        
        



#f.close()
#cv.waitKey(0)
#print(len(calculate_coordinates(contours,num*offsetValue)))
cv.destroyAllWindows()
