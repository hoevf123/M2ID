# MapleStory2 Image Devider
# You MUST need a square size of picture

# Made by. the Clock says tick tock
# Python 2.7.12
# You must need PIL
# You may install with "pip install Pillow" on cmd


from PIL import Image

def imageProcessor(rawImage, i, j, n, m, Mode = 0):
    result = Image.new("RGB", (1024, 1024), "white")
    width = rawImage.size[0] / n
    height = rawImage.size[1] / m
    resizeImage = rawImage.crop((j*width, i*height, j*width+width, i*height+height))

    if Mode == 0: #block
        resizeImage = resizeImage.resize((226, 226), Image.ANTIALIAS)
        result.paste(resizeImage, (287,441))
    elif Mode == 1: #flat
        resizeImage = resizeImage.resize((360, 360), Image.ANTIALIAS)
        result.paste(resizeImage, (156,410))
        
    saveFileName = "result" + str(i) + str(j) + ".png"
    print "Save image", saveFileName
    result.save(saveFileName)

inputImageName = raw_input("Input File Name include extension. ex) image.png\n")
inputImage = Image.open(inputImageName)
print "image size is ", str(inputImage.size[0]),"x", str(inputImage.size[1])

print "We will devide image with NxM (with N columns, M rows)"
print "input N in integer"
n = int(input())
print "input M in integer"
m = int(input())

if n >= 10 or m >= 10:
    print "NOTICE!! I recommend n and m would be smaller than 10 due to file name system"

if ((n == m) & (inputImage.size[0] != inputImage.size[1])):
    print "NOTICE!! input image is not a square size!"

mode = int(raw_input("Block or Flat?\nInput 0 for block\nInput 1 for flat\n"))

for i in range(n):
    for j in range(m):
        imageProcessor(inputImage, j, i, n, m, mode)

raw_input("Done! Press any Key to continue...")
