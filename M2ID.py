# MapleStory2 Image Devider
# Made by. the Clock says tick tock
# Python 2.7.12
# You must need PIL
# You may install with "pip install Pillow" on cmd


from PIL import Image

def imageProcessor(rawImage, i, j, n, m, Mode = 0):
    result = Image.new("RGB", (1024, 1024), "white")
    width = rawImage.size[0] / n
    height = rawImage.size[1] / m
    if height > width:
        height = width
    elif width > height:
        width = height
    
    resizeImage = rawImage.crop((j*width, i*height, j*width+width, i*height+height))

    if Mode == 0: #block
        resizeImage = resizeImage.resize((230, 230), Image.ANTIALIAS)
        result.paste(resizeImage, (286,438))
    elif Mode == 1: #flat
        resizeImage = resizeImage.resize((360, 360), Image.ANTIALIAS)
        result.paste(resizeImage, (156,410))
    elif Mode == 2: #block upper face
        resizeImage = resizeImage.resize((229, 229), Image.ANTIALIAS)
        result.paste(resizeImage, (285,213))
        # some addition : left side
        tmpImage = resizeImage.crop((0,0,6,228))
        tmpImage = tmpImage.resize((229,229),Image.ANTIALIAS)
        tmpImage = tmpImage.rotate(90)
        tmpImage = tmpImage.resize((229,7),Image.ANTIALIAS)
        result.paste(tmpImage, (55, 438))

        # some addition : right side
        tmpImage = resizeImage.crop((222,0,228,228))
        tmpImage = tmpImage.resize((229,229),Image.ANTIALIAS)
        tmpImage = tmpImage.rotate(270)
        tmpImage = tmpImage.resize((229,7),Image.ANTIALIAS)
        result.paste(tmpImage, (514,438))

        # some addition : down side
        tmpImage = resizeImage.crop((0,226,228,228))
        result.paste(tmpImage, (285,442))
        
        
        
    saveFileName = "result" + str(i) + str(j) + ".png"
    print "Save image", saveFileName
    result.save(saveFileName)

inputImageName = raw_input("Input File Name include extension. ex) image.png\n")
inputImage = Image.open(inputImageName)
print "image size is ", str(inputImage.size[0]),"x", str(inputImage.size[1])

print "Devide image with NxM (with N columns, M rows)"
print "input N in integer"
n = int(input())
print "input M in integer"
m = int(input())

if n >= 10 or m >= 10:
    print "NOTICE!! I recommend n and m would be smaller than 10 due to file name system"

mode = int(raw_input("Mode Selection\n0 : Block (Side face)\n1 : Flat (Side face)\n2 : Block (Upper face)\n"))

w = inputImage.size[0]/n
h = inputImage.size[1]/m
if w > h:
    w = h
    print 100 - w*n*100/inputImage.size[0], "% lost for width"
else:
    h = w
    print 100 - h*m*100/inputImage.size[1], "% lost for height"

tmpImage = inputImage.crop((0,0,w*n,h*m))
tmpImage.save("result.png")

for i in range(n):
    for j in range(m):
        imageProcessor(inputImage, j, i, n, m, mode)

raw_input ("Press Enter to Continue...")
