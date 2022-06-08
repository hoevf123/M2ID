# MapleStory2 Image Devider
# Made by. the Clock says tick tock
# Python 2.7.12
# You must need PIL, numpy
# You may install with "pip install Pillow" on cmd

'''
THIS PROGRAM is PERMITED modifying, distributing this program as open source WITH Commenting Original program creater/developer's Name(KMS2 지뉴, inven Nickname 시계는째깍)
MAPLESTORY2 INVEN SOURCE POST URL : http://www.inven.co.kr/board/maple2/4276/6160
Github REPOSITIORY(Airplaner/M2ID) MASTER BRANCH URL : https://github.com/Airplaner/M2ID/
Original Programmer(지뉴) Contact : (Discord) Airplaner#7961
THIS PROGRAM FORKED PURPORSE to adding more comportable DESIGN TEMPLATE MODIFICATION function(s).

modified program with compatible at python 3
modifier : hoevf123@github.com (KMS2 비숍의하루)
first fork and modified date : 2020-10-27
last modified date : 2020-10-28
forked project's Github URL : https://github.com/hoevf123/M2ID
tested circumstance : python 3.8.6 (VSCode) / python 3.8.6 (python internal IDLE) / python 3.8.6 (windows 10 python console)
contact : hoevf123@naver.com / hoevf123.dongs@gmail.com / (KMS2 letter available) 스카니아 - 비숍의하루 / (Discord) 비숍의하루#5686

modified info (2020-10-27)
- added "floor panel" upper face copy function
- raw_input functioned as python3 input function
- imported os module to set current file's location
- added transparentable background color initialization with RGBA type hex(or decimal tuple) value preprocessing with string to hex conversion function or PIL default strings.
  (default value to skip defining colour, default : white)
- changed file naming system(file format) with mixing A-Z(26-ximal big alphabetical numberic system) as row, 0-9(decimal numberic system) as column, with heading origin filename.
  (result_12.png -> origin_result_B2.png)
  due to changing result naming system, removed naming alert when divided over 10 rows or columns.

modified info (2020-11-03)
- added copyright from original programmer's request.
- added original programmer's contact info. (with corrected wrong original's KMS2 character name "지뉴느님" to "지뉴")
- need "numpy" module if this version runs.
- renewaled M2ID functions
    ====================================================
    Mode Selection\n
    [CUBE]
    0 : Design Cube (Front face)
    1 : Design Cube (Upper face)
    2 : Design Cube Surrounding Side face / Rotating Block (4 faces, at most 4 image files required)
    [FLAT CUBE]
    3 : Design Divider Cube (flat) (Front face)
    4 : Design (Broad) Rectangle Cube (flat) (Front face)
    5 : [NOT SUPPORTED IN THIS PROGRAM] Design Arch Piliar Cube (Front face) # Not Supported beause of the Edge processing problem.
    [FLOOR CUBE]
    6 : Design Arch Ceiling Cube (Upper face)
    7 : Design Floor Panel Cube (Upper face)
    WARNING TO TREAT(Design Arch Type Cubes) : [FRONT FACE, CURVED] <-- [UPPER FACE] -> [BACK FACE]]
    8 : Design Arch Type Cube (Upper face)
    9 : Design Arch Type Cube (Upper face, 180 degree)
    10 : Design Arch Type Cube (Upper face, 90 degree, reverse 'r' type direction)
    11 : Design Arch Type Cube (Upper face, 270 degree, 'r' type direction)
    12 : [NOT SUPPORTED IN THIS PROGRAM] Design Arch Type Cube (Back face) # Not Supported beause of the Edge processing problem.
    =====================================================
- changed user keyborard input orders 
    FROM
    [image name input] -> [background color input] -> [N x M divide number input] -> [Mode Selection]
    TO
    [Mode Selection] -> [image name input(multiple imput if specific mode requires)] -> [background color input] -> [N x M divide number input]
    to support multiple value input.
- imageProcesser function input can be input arguments as tuple, list of multiple images(or None).
- added or modified bunch of irritatable processing messages.
- added image skewing functions(copied from stackoverflow.com web site). but, it's deprecated because of the Mode 12 function implementation failure.


modified info (2020-11-17)
- fixed(swapped) the rownums and colnums are swapped. (and defined row and col names definition)
- fixed transparent image sets to transparent color, correction to overlayed background color. (changed paste method to alpha_composite method)
- changed Program Exit print message when image processing is done. (M2ID origin user's request at comment)
- added image description, contained to the github readme.md

modified info (2020-12-08)
- fixed bugs to not working image process when non-transparentive image file(s) input.
- NxM value input can be skipped with default value when you're enter wrong value or Nothing
- Updated readme.md for changed NxM division Method

further, will de developing...
- multiple image input support(repeatable work available)
- program execution with argument(s) support (argv)
  (so, i'm trying to skip input file or directory name(s) when argv is input at required 0 remaining image file request(s))
- replaced result file saved at source file placing directory(on first file in work progress)
- file input available by directory(folder), proceed all files in current working directory(NOT RECURSIVE)

'''

from PIL import Image
import os   # to set default running location
import sys  # to get Uncaught Error Message(s).
import math # to use log calculation
#import numpy  # to use matrix calculation (skewing function)

# Set File's Current real location 
# (if this code not exist, like VSCode, Sets default starting location to System32 NOT Current file placed location)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

global raw_input

try:
    if not(raw_input == None):
        pass
except(NameError):
    raw_input = input


def raw_inputImage(message, skip=False):
    isFileFound = False
    inputImage = None
    while(not isFileFound):
        inputImageName = raw_input(message)
        try:
            if(skip == True and inputImageName.strip() == ""):
                break
            inputImage = Image.open(inputImageName)
            isFileFound = True
        except(FileNotFoundError):
            print("file name " + str(inputImageName) + " invalid name or NOT FOUND. TRY AGAIN.")
        except:
            print(sys.exc_info())
            print("failed to input image file because of internal function error. (raw_inputImage)")
            break
    
    return inputImage
    
def raw_inputImages(message, requestTimes, skip=False):
    ret_inputImages = []
    remainingTimes = requestTimes - 1
    while(0 <= remainingTimes):
        ret_inputImage = [raw_inputImage(str(message).replace(str("%d"), str(remainingTimes)) ,skip)]
        remainingTimes -= len(ret_inputImage)
        ret_inputImages.extend(ret_inputImage)

    return ret_inputImages

def int_input(message="", default_value=None):
    #Convert 0-9 Decimal number to integer value as string
    string_number_values = (raw_input(message).replace("  ", " ").strip().split(" "))
    ret_value = default_value
    for string_number_value in string_number_values:
        try:
            ret_value = int(string_number_value)
        except:
            print(sys.exc_info())
            print("Number Conversion Error :", string_number_value , " so ret_value sets to default value %d" % (ret_value,))
            pass
        break
    return ret_value
        
    

# copied function from https://stackoverflow.com/questions/14177744/how-does-perspective-transformation-work-in-pil
# copied and referenced function from https://stackoverflow.com/questions/14177744/how-does-perspective-transformation-work-in-pil
# skewing function
# def find_coeffs(src_points, dest_points):
#     matrix = []
#     for p1, p2 in zip(src_points, dest_points):
#         matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
#         matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

#     A = numpy.matrix(matrix, dtype=numpy.float)
#     B = numpy.array(dest_points).reshape(8)

#     res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
#     return numpy.array(res).reshape(8)

def str_to_hexlist(str_hex):
    str_hex = str(str_hex).replace(" ", "").replace("\"", "").replace("\'", "")
    list_hex = None
    if(str_hex.startswith("0x") or str_hex.startswith("#")):
        str_hex = str_hex[2:] # removes "0x" Symbol
    if(str_hex.startswith("(")): # it considers as decimal value of color
        list_hex = []
        str_hex = str_hex[0:str_hex.find(")")]
        list_dec = str_hex[1:].split(",", 4) # (R,G,B,A)

        class NOT_RGB_FORMAT(Exception): # Custom Exception class just for rasing incorrect RGB(A) format.
            def __init__(self, target_rgb_format):
                self.target_rgb_format = target_rgb_format
                pass
            def __str__(self):
                return "Value Must Be at least 3 elements. you got only "+ len(self.target_rgb_format) +" Elements. " + self.target_rgb_format 
        try:
            if(len(list_dec) < 3):
                raise NOT_RGB_FORMAT(list_dec)
            for a in list_dec:
                list_hex.append(int(a) % 256)
        except(NOT_RGB_FORMAT):
            print(sys.exc_info())
            print("NOT RGB FORMAT DETECTED")
            list_hex = None
    else:
        # Typed as hex 3,4,6,8, digits or just normal string
        str_hex = str_hex.replace(" ", "")
        if(len(str_hex) in [3,4,6,8]):
            str_len = len(str_hex)
            def str_to_hex(str_char):
                str_char = str(str_char).strip()
                if(str_char.startswith("0x")):
                    str_char = str_char[2:] # remove head "0x" word
                hex_result = 0
                for a in str_char:
                    a = a.lower()
                    hex_result = hex_result * 16
                    if a in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        hex_result = hex_result + int(a)
                    elif a in ["a", "b", "c", "d", "e", "f"]:
                        hex_result = hex_result + ord(a) - ord("a") + 10
                    else:
                        hex_result = None
                        break
                return hex_result

            if str_len == 3: #(R, G, B)
                list_hex=[str_to_hex(str_hex[0]), str_to_hex(str_hex[1]), str_to_hex(str_hex[2])]
            elif str_len == 4: #(R, G, B, A)
                list_hex=[str_to_hex(str_hex[0]), str_to_hex(str_hex[1]), str_to_hex(str_hex[2]), str_to_hex(str_hex[3])]
            elif str_len == 6: #(RR, GG, BB)
                list_hex=[str_to_hex(str_hex[0:2]), str_to_hex(str_hex[2:4]), str_to_hex(str_hex[4:6])]
            elif str_len == 8: #(RR, GG, BB, AA)
                list_hex=[str_to_hex(str_hex[0:2]), str_to_hex(str_hex[2:4]), str_to_hex(str_hex[4:6]), str_to_hex(str_hex[6:8])]
            if list_hex == None or (None in list_hex):
                list_hex = None

    return list_hex

def signedint_to_alphabetString(value_int):
    digit = 26 # count of A-Z letters(UpperCase Only), sum of 26 alphabets.
    result_letter=""
    if not(str(value_int).isdecimal()):
        return None
    if(value_int < 0): # convert minus value to adjacent maximum modular plus value. (ex : -26 => 500)
        result_letter = "-" # attach minus symbol
        mulpliy_counts = int(math.log(digit, -value_int)) + 1
        value_int = (digit ** mulpliy_counts) - value_int
    while(value_int >= 0):
        result_letter = chr(value_int % digit + 65) + result_letter
        value_int = int(value_int / digit)
        if(value_int <= 0):
            break
    return result_letter
            


def imageProcessor(rawImage_origin, i, j, n, m, Mode = 0, fill="white"):
    # rawImage variable can be Image type of Sets of Image types
    if(fill == None or fill == ""):
        fill="white"
    fill_hex_list = str_to_hexlist(fill)
    if not(fill_hex_list == None):
        fill = fill_hex_list
    if isinstance(fill, (list, set)):
        fill = tuple(fill)
    try:
        result = Image.new("RGBA", (1024, 1024), fill)
    except:
        print(sys.exc_info())
        print("input fill value : ", fill)
        print("Error input. fill sets to default color.")
        result = Image.new("RGBA", (1024, 1024), "white")
    
    rawImages = []
    # convert single Image Input value to list item.
    if isinstance(rawImage_origin, (list, set, tuple)):
        rawImages = rawImage_origin
    else:
        rawImages.append(rawImage_origin)

    # Set Remaining Face
    remainingFace = 1
    if (Mode == 2):
        remainingFace = 4   # Required 4 Face to Paint

    for rawImage in rawImages:
        if remainingFace <= 0:
            print("break ya")
            break
        
        # Remaining Face Decreasing(Including None Image(s))
        remainingFace = remainingFace - 1
        print("Mode "+ str(Mode) + " Processing.. (Remaining Face : " + str(remainingFace) + ")")

        # Skip painting when image is None.
        if rawImage == None:
            print("Skipped Image because of Void or Not Image input.")
            continue

        # adjust something?
        width = rawImage.size[0] / n
        height = rawImage.size[1] / m
        if height > width:
            height = width
        elif width > height:
            width = height
        
        resizeImage = rawImage.crop((j*width, i*height, j*width+width, i*height+height))

        # forces image types to RGBA type to use alpha_compositie method cause of mapping alpha color directly.
        resizeImage = resizeImage.convert("RGBA")

        ####
        # CUBE(S)
        # 0 : Design Cube front face
        # 1 : Design Cube upper face
        # 2 : Design Cube Surrounding Side face / Rotating Block (4 faces)
        ####

        if Mode == 0: # Design Cube front face
            resizeImage = resizeImage.resize((230, 230), Image.ANTIALIAS)
            result.alpha_composite(resizeImage, (286,438))

        elif Mode == 1: # Design Cube upper face
            resizeImage = resizeImage.resize((229, 229), Image.ANTIALIAS)
            result.alpha_composite(resizeImage, (285,213))
            # some addition : left side
            tmpImage = resizeImage.crop((0,0,6,228))
            tmpImage = tmpImage.resize((229,229),Image.ANTIALIAS)
            tmpImage = tmpImage.rotate(90)
            tmpImage = tmpImage.resize((229,7),Image.ANTIALIAS)
            result.alpha_composite(tmpImage, (55, 438))

            # some addition : right side
            tmpImage = resizeImage.crop((222,0,228,228))
            tmpImage = tmpImage.resize((229,229),Image.ANTIALIAS)
            tmpImage = tmpImage.rotate(270)
            tmpImage = tmpImage.resize((229,7),Image.ANTIALIAS)
            result.alpha_composite(tmpImage, (514,438))

            # some addition : down side
            tmpImage = resizeImage.crop((0,226,228,228))
            result.alpha_composite(tmpImage, (285,442))

        elif Mode == 2: # Design Cube Surrounding Side face / Rotating Block (4 faces)
            BLOCKSIZE = 227
            if remainingFace == 3:
                resizeImage = resizeImage.resize((BLOCKSIZE, BLOCKSIZE), Image.ANTIALIAS)
                result.alpha_composite(resizeImage, (57,440))
            elif remainingFace == 2:
                resizeImage = resizeImage.resize((BLOCKSIZE, BLOCKSIZE), Image.ANTIALIAS)
                result.alpha_composite(resizeImage, (57+BLOCKSIZE,440))
            elif remainingFace == 1:
                resizeImage = resizeImage.resize((BLOCKSIZE, BLOCKSIZE), Image.ANTIALIAS)
                result.alpha_composite(resizeImage, (57+2*BLOCKSIZE,440))
            elif remainingFace == 0:
                resizeImage = resizeImage.resize((BLOCKSIZE, BLOCKSIZE), Image.ANTIALIAS)
                result.alpha_composite(resizeImage, (57+3*BLOCKSIZE,440))

        ####
        # FLAT CUBE(S)
        # WARNING TO TREAT(ALL FLAT CUBE(S)) : [void area] <-- [FRONT FACE] <-- [BLOCK OBJECT(WALL)] --> [BACK FACE]  
        # 3. Design Divider Cube (front face)
        # 4. Design (Broad) Rectangle Cube (front face)
        # 5. [NOT SUPPORTED IN THIS PROGRAM] Design arch piliar Cube (front face)
        ####

        elif Mode == 3: #divider cube (flat type) front face
            resizeImage = resizeImage.resize((360, 360), Image.ANTIALIAS)
            result.alpha_composite(resizeImage, (156,410))
        
        elif Mode == 4: #broad rectangle cube (flat type) front face
            resizeImage = resizeImage.resize((304, 304), Image.ANTIALIAS)
            result.alpha_composite(resizeImage, (214,456))
            pass

        elif Mode == 5: #arch piliar cube (flat type) front face
            print("NOT SUPPORTED IN THIS PROGRAM")
            return

            resizeImage = resizeImage.resize((294, 294), Image.ANTIALIAS)

            # face 1 : front face
            tmpImage = resizeImage.crop((0,3,294,294))
            result.alpha_composite(tmpImage, (512,480))

            # face 2 : edge 4px
            tmpImage = resizeImage.crop((0,0,294,6))
            tmpImage = tmpImage.rotate(90, expand=True)
            result.alpha_composite(tmpImage, (512,188))
            pass

        ####
        # FLOOR CUBE(S)
        # 6 : Design Arch Ceiling Cube (Upper face)
        # 7 : Design Floor Panel Cube (Upper face)
        # WARNING TO TREAT(Design Arch Type Cubes) : [FRONT FACE, CURVED] <-- [UPPER FACE] -> [BACK FACE]]
        # 8 : Design Arch Type Cube (Upper face)
        # 9 : Design Arch Type Cube (Upper face, 180 degree)
        # 10 : Design Arch Type Cube (Upper face, 90 degree, reverse 'r' type direction)
        # 11 : Design Arch Type Cube (Upper face, 270 degree, 'r' type direction)
        # 12 : Design Arch Type Cube (Back face)
    
        ####

        elif Mode == 6: #Arch Ceiling Cube (Upper face)
            resizeImage = resizeImage.resize((294, 294), Image.ANTIALIAS)
            result.alpha_composite(resizeImage, (447,238))
            pass
        
        elif Mode == 7: #floor panel upper face
            # NOTE: need helps to adjusting edge modification
            resizeImage = resizeImage.resize((342, 342), Image.ANTIALIAS)
            result.alpha_composite(resizeImage, (347,144))

        elif Mode == 8: #Arch Type Cube (Upper face)
            resizeImage = resizeImage.resize((224, 224), Image.ANTIALIAS)
            result.alpha_composite(resizeImage, (507,275))
            pass

        elif Mode == 9: #Arch Type Cube (Upper face, 180 degree)
            resizeImage = resizeImage.resize((224, 224), Image.ANTIALIAS)
            resizeImage = resizeImage.rotate(180)
            result.alpha_composite(resizeImage, (507,275))
            pass

        elif Mode == 10: #Arch Type Cube (Upper face, 90 degree, reverse 'r' type direction)
            resizeImage = resizeImage.resize((224, 224), Image.ANTIALIAS)
            resizeImage = resizeImage.rotate(90)
            result.alpha_composite(resizeImage, (507,275))
            pass

        elif Mode == 11: #Arch Type Cube (Upper face, 270 degree, reverse 'r' type direction)
            resizeImage = resizeImage.resize((224, 224), Image.ANTIALIAS)
            resizeImage = resizeImage.rotate(270)
            result.alpha_composite(resizeImage, (507,275))
            pass

        elif Mode == 12: #Arch Type Cube (Back face)
            print("This Function Is Currently NOT Supported")
            return
            # Origin : Main face 
            
            resizeImage = resizeImage.resize((224, 224), Image.ANTIALIAS)

            # Part 1 : Main face ((0,4) to (224, 224))
            tmpImage = resizeImage.crop((0,4,224,222))
            result.alpha_composite(tmpImage, (68,496))

            # Part 2 : top face ((0,0) to (224,2))
            tmpImage = resizeImage.crop((4,0,220,4))
            tmpImage = tmpImage.resize((224, 4))
            #tmpImage = tmpImage.transform((226,4), Image.AFFINE, data=find_coeffs([(0,0), (224,0), (224,4),(0,4)], [(0,0), (228,0), (228,4), (0,4)]))
            tmpImage = tmpImage.rotate(180)

            result.alpha_composite(tmpImage, (507,275))
            pass
    
    current_file_name=""
    if not (rawImages == None or rawImages[0] == None):
        current_file_name = rawImages[0].filename
    if not(current_file_name == ""):
        current_file_name = current_file_name[:current_file_name.rfind(".")]
        current_file_name = current_file_name.replace("../", "   ").replace("./", "  ")[current_file_name.rfind("/") + 1:]

    '''
    SAVEFILE RULE about coordinates
        A    B    C    ... (column number as index j, use as FIRST STARTS 'A' to 'Z' symbol)
    0 (0,0)(0,1)(0,2)
    1 (1,0)(1,1)(1,2)
    2 (2,0)(2,1)(2,2)
    ...
    (row number as index i, use as FIRST STARTS '0' to '9' symbol)

    Example of CROPPED SAVEFILE NAME
    The filename of B2(2,1) is "(blahblah as FILENAME)_resultB2.png"
    '''
    
    saveFileName = str(current_file_name) + "_result" + str(signedint_to_alphabetString(int(j))) + str(i) + ".png" # i as row(vertical) number, j as column(horizontal) number
    print("Saved Design Template image file : ", saveFileName)
    result.save(saveFileName)


print("""
M2ID(Maplestory2 Image Devider) by Airplaner(지뉴 in KMS2), mod by 비숍의하루.
Last Modified : 2020. 11. 17.
This Program is forced Open Source policy, can be distributed and modded for any purpose with just remarking origin owner(지뉴) on source code and distribution.
for any Question : (Discord, Forked Branch) 비숍의하루#5686 / (Discord, Master Branch) Airplaner#7961

Github repository URLs.
- Airplaner/M2ID (MASTER BRANCH) : https://github.com/Airplaner/M2ID/   
- hoevf123/M2ID (forked Project, This Program) : https://github.com/hoevf123/M2ID
""")

mode = 0
trial = 0
max_trial = 3
while(True):
    mode = int(raw_input("""
====================================================
Mode Selection\n
[CUBE]
0 : Design Cube (Front face)
1 : Design Cube (Upper face)
2 : Design Cube Surrounding Side face / Rotating Block (4 faces, at most 4 image files required)
[FLAT CUBE]
3 : Design Divider Cube (flat) (Front face)
4 : Design (Broad) Rectangle Cube (flat) (Front face)
5 : [NOT SUPPORTED IN THIS PROGRAM]
[FLOOR CUBE]
6 : Design Arch Ceiling Cube (Upper face)
7 : Design Floor Panel Cube (Upper face)
WARNING TO TREAT(Design Arch Type Cubes) : [FRONT FACE, CURVED] <-- [UPPER FACE] -> [BACK FACE]]
8 : Design Arch Type Cube (Upper face)
9 : Design Arch Type Cube (Upper face, 180 degree)
10 : Design Arch Type Cube (Upper face, 90 degree, reverse 'r' type direction)
11 : Design Arch Type Cube (Upper face, 270 degree, 'r' type direction)
12 : [NOT SUPPORTED IN THIS PROGRAM]
=====================================================

Your Choose Mode Number > """))
    if(mode in [0,1,2,3,4,6,7,8,9,10,11]):
        break

    print("Your Input " , mode, "is INVALID. Try again Correct Input Mode", "(" + str(max_trial - trial) + " attempt(s) remaining)")

    if max_trial - trial <= 0:
        print("M2ID PROGRAM CLOSED [Reason : wrong Input Mode inputs]")
        raw_input ("Press Enter to Continue...")    
        exit() # finalize program.
    else:
        trial = trial + 1

# FILE NAME INPUT
print("Current Directory's Including File")
print(os.listdir())

# in normal mode, 1 image requies.
need_imagefileCounts = 1
if mode == 2: # Mode 2 Requires 3 more images. (total 4)
    need_imagefileCounts = 4

inputImage = list(raw_inputImages("Input File Name including extension. ex) image.png (reamining %d more Images, just PRESS Enter to skip) > ", need_imagefileCounts, skip=True))




# BACKGROUND COLOR SETTING
print("background initializing value input (just enter to set white)")
bg_color = raw_input("[ex : input type : ff00ff or green or (255,0,255,120)]\n#NOTE : NOT ALLOWED WITHOUT BRACELET comma phrase (EX : \"0,1,0\")\n")
if(bg_color==""):
    pass
else:
    if(bg_color.startswith("#")):
        bg_color=bg_color[1:9]
        
# IMAGE DIVIDING VALUE INPUT
default_row_value = 1
default_column_value = 1
print("Divide image with NxM (with N columns, M rows)")
print("input N column(s) in integer (skip to default value : %d)" % (default_column_value,))
n = abs(int_input(default_value=default_column_value))
print("input M row(s)in integer (skip to default value : %d)" % (default_row_value,))
m = abs(int_input(default_value=default_row_value))




# Modulize main function to Support multiple file group processing
def makeImageProcess(mode, inputImage, n, m, bg_color):
    # save each images with cropped result(NOT USED TO PASTE Result Design Templates)
    # IMAGE CROP INGREDIENT PREPARATION AND NAME RESULT FILE
    tmpImages = []

    print(type(inputImage))
    if isinstance(inputImage, (list, set, tuple)):
        tmpImages = inputImage
    else:
        tmpImages.append(inputImage)

    for arg_inputImage in tmpImages:
        #if not(isinstance(inputImage, Image)):
        if arg_inputImage == None:
            continue
        inputImageName = arg_inputImage.filename
        w = arg_inputImage.size[0]/n
        h = arg_inputImage.size[1]/m

        print("Image file " + str(inputImageName) + " size is ", str(arg_inputImage.size[0]),"x", str(arg_inputImage.size[1]))
        # fit cropped image to width or height and then show result of cropped origin image size
        if w > h:
            w = h
            print("Image file " + str(inputImageName) + " :: " + str(100 - w*n*100/arg_inputImage.size[0]), "% lost for width")
        else:
            h = w
            print("Image file " + str(inputImageName) + " :: " + str(100 - h*m*100/arg_inputImage.size[1]), "% lost for height")

        # save cropped origin image
        tmpImage = arg_inputImage.crop((0,0,w*n,h*m))
        resultorigin_imageName = inputImageName[:inputImageName.rfind(".")][inputImageName.replace("../", "   ").replace("./","  ").rfind("/") + 1:] + "_result.png"
        tmpImage.save(resultorigin_imageName)
        print("Saved Cropped origin image :: " + resultorigin_imageName)

    for i in range(n):
        for j in range(m):
            imageProcessor(inputImage, j, i, n, m, mode, bg_color)


# make workload queue
if not isinstance(inputImage,(list, tuple, set)):
    inputImage = list(inputImage)

processImageQueue = []
index_i = 0
index_div_col = -1
index_div_row = -1
len_inputImage = len(inputImage)
while(index_i < len_inputImage):
    if(index_i % len_inputImage == 0):
        processImageQueue.append([])
        index_div_row += 1
        index_div_col = 0
    processImageQueue[int(index_div_row)].append(inputImage[index_i])
    index_i += 1
    index_div_col += 1

# process made workload queue by list
for sequence_inputImage in processImageQueue:
    makeImageProcess(mode, sequence_inputImage, n, m, bg_color)

raw_input ("Press Enter to Exit...")
