#ej3.py
#Por Luis Diego Fernandez
import sys
import math
import bmp_maker

# image attributes
width = 800
height = 600
x_to_paint = 1
y_to_paint = 1
bits_per_pixel = 32

newBmpImage = bmp_maker.bmpImage()
newBmpImage.glCreateWindow(width, height)
newBmpImage.glClearColor(0,0,0)
newBmpImage.glColor(1,1,1);
newBmpImage.glClear()

newBmpImage.glLine(-0.975,0.967,0.275,0.967)
newBmpImage.glLine(-0.975,0.967,0.155,0.363)
newBmpImage.glLine(-0.975,0.967,-0.114,-0.180)
newBmpImage.glLine(-0.975,0.967,-0.523,-0.54)
newBmpImage.glLine(-0.975,-0.7,-0.975,0.967)

newBmpImage.glFinishWN("ej3.bmp")

print("Done")
