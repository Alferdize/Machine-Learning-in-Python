confThreshold= 0.5
nmsThreshold = 0.4
inpWidth = 416
inpHeight = 416

classesFile = "coco.names"
classes = None
with open(classesFile,"rt") as f:
    classes = f.read().rstrip("\n").split("\n")
print(classes)