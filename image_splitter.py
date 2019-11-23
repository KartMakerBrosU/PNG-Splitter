import cv2
import sys

def splitimage(sidepixels, original_img, returnfilename):

    height = original_img.shape[0]
    width = original_img.shape[1]
    extention = ".png"
    counter = -1
    
    for i in range(0,width,sidepixels):
        for j in range (0,height, sidepixels):
            temp_img = original_img[j:j + sidepixels, i:i+sidepixels]

            counter = counter + 1
            newfilename = returnfilename + "." + str(counter) + extention
            
            cv2.imwrite(newfilename,temp_img)
            


def bail(message):
    print(message)
    input("\nPress Enter to exit")

print ("PNG Splitter v1.1")
print ("\nInput the file name")
filename = input("")
print ("Input the size of the image (square)")
try:
    sidepixels = int(input(""))
except ValueError:
    bail("Nope, has to be an integer. Restart the program")
print ('Input result name without ".png" extention')
print ('Result name will be "INPUT.0.png"')
returnfilename = input("")
original_img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
images = splitimage(sidepixels, original_img, returnfilename)
