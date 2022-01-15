import os
from PIL import Image
import glob, os

imagesThing = [name for name in os.listdir("./icons/hicolor/") if (os.path.isdir("./icons/hicolor/"+name) and (len(name.split("x")) >1) and name.split("x")[0] == name.split("x")[1])]
resolution = [name.split("x")[1] for name in os.listdir("./icons/hicolor/") if (os.path.isdir("./icons/hicolor/"+name) and (len(name.split("x")) >1) and name.split("x")[0] == name.split("x")[1])]
#print(os.listdir("./icons/hicolor/"))
print(imagesThing)
print(resolution)
for i in imagesThing:
    for infile in glob.glob("./icons/hicolor/"+i+"/apps/*.png"):
        stuff = os.path.join(infile)
        file, ext = os.path.splitext(stuff)
        print(file,ext)