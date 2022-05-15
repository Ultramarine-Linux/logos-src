import os
import sys

# cd to icons folder
os.chdir("icons/hicolor")

# for each folder in hicolor
for folder in os.listdir("."):
    # cd to folder
    os.chdir(folder)
    # cd to apps folder
    os.chdir("apps")
    # for every file named fedora-logo-icon.png
    for file in os.listdir("."):
        if file == "fedora-logo-icon.png":
            # copy the file as ultramarine.png
            os.system("cp " + file + " ultramarine.png")
    # cd back to hicolor
    os.chdir("../..")