# MapleStory2 Image Devider
# Made by. the Clock says tick tock
# Python 2.7.12
# You must need PIL
# You may install with "pip install Pillow" on cmd

'''
COMMENT : this program is NOT permitted to modifying this program by program creater/developer(KMS2 지뉴느님, inven Nickname 시계는째깍)
MAPLESTORY2 INVEN SOURCE POST URL : http://www.inven.co.kr/board/maple2/4276/6160
Github REPOSITIORY(Airplaner/M2ID) MASTER BRANCH URL : https://github.com/Airplaner/M2ID/
THIS PROGRAM FORKED PURPORSE to adding more comportable DESIGN TEMPLATE MODIFICATION function(s).

modified program with compatible at python 3
modifier : hoevf123@github.com (KMS2 비숍의하루)
modified date : 2020-10-27
tested circumstance : python 3.8.6 (VSCode) / python 3.8.6 (python internal IDLE) / python 3.8.6 (windows 10 python console)
contact : hoevf123@naver.com / hoevf123.dongs@gmail.com / (KMS2 letter available) 스카니아 - 비숍의하루 / (Discord) 비숍의하루#5686

modified info
- added "floor panel" upper face copy function
- raw_input functioned as python3 input function
- imported os module to set current file's location
- added transparentable background color initialization with RGBA type hex(or decimal tuple) value preprocessing with string to hex conversion function or PIL default strings.
  (default value to skip defining colour, default : white)
- changed file naming system(file format) with mixing A-Z(26-ximal big alphabetical numberic system) as row, 0-9(decimal numberic system) as column, with heading origin filename.
  (result_12.png -> origin_result_B2.png)
  due to changing result naming system, removed naming alert when divided over 10 rows or columns.
'''

from PIL import Image
import os   # to set default running location
import sys  # to get Uncaught Error Message(s).
import math # to use log calculation

# Set File's Current real location 
# (if this code not exist, like VSCode, Sets default starting location to System32 NOT Current file placed location)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

global raw_input

try:
    if(raw_input == None):
        pass
except(NameError):
    raw_input = input

class NOT_RGB_FORMAT(Exception):
    def __init__(self, target_rgb_format):
        self.target_rgb_format = target_rgb_format
        pass
    def __str__(self):
        return "Value Must Be at least 3 elements. you got only "+ len(self.target_rgb_format) +" Elements. " + self.target_rgb_format 


def str_to_hexlist(str_hex):
    str_hex = str(str_hex).replace(" ", "").replace("\"", "").replace("\'", "")
    list_hex = None
    if(str_hex.startswith("0x") or str_hex.startswith("#")):
        str_hex = str_hex[2:] # removes "0x" Symbol
    if(str_hex.startswith("(")): # it considers as decimal value of color
        list_hex = []
        str_hex = str_hex[0:str_hex.find(")")]
        list_dec = str_hex[1:].split(",", 4) # (R,G,B,A)
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
        str_current_i = 0
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

            if str_len == 3:
                list_hex=[str_to_hex(str_hex[0]), str_to_hex(str_hex[1]), str_to_hex(str_hex[2])]
            elif str_len == 4:
                list_hex=[str_to_hex(str_hex[0]), str_to_hex(str_hex[1]), str_to_hex(str_hex[2]), str_to_hex(str_hex[3])]
            elif str_len == 6:
                list_hex=[str_to_hex(str_hex[0:2]), str_to_hex(str_hex[2:4]), str_to_hex(str_hex[4:6])]
            elif str_len == 8:
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
        mulpliy_counts = int(math.log(digit, -value_int)) + 1
        value_int = (digit ** mulpliy_counts) - value_int
    while(value_int >= 0):
        result_letter = chr(value_int % digit + 65) + result_letter
        value_int = int(value_int / digit)
        if(value_int <= 0):
            break
    return result_letter
            


def imageProcessor(rawImage, i, j, n, m, Mode = 0, fill="white"):
    if(fill == None or fill == ""):
        fill="white"
    fill_hex_list = str_to_hexlist(fill)
    if not(fill_hex_list == None):
        fill = fill_hex_list
    if(type(fill) is list):
        fill = tuple(fill)
    try:
        result = Image.new("RGBA", (1024, 1024), fill)
    except:
        print(sys.exc_info())
        print("input fill value : ", fill)
        print("Error input. fill sets to default color.")
        result = Image.new("RGBA", (1024, 1024), "white")
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
    elif Mode == 3: #floor panel upper face
        # NOTE: need helps to adjusting edge modification
        resizeImage = resizeImage.resize((342, 342), Image.ANTIALIAS)
        result.paste(resizeImage, (347,144))

        
        
    current_file_name = rawImage.filename
    if current_file_name == None:
        current_file_name = ""
    if not(current_file_name == ""):
        current_file_name = current_file_name[:current_file_name.rfind(".")]
        current_file_name = current_file_name.replace("../", "   ").replace("./", "  ")[current_file_name.rfind("/") + 1:]
    
    saveFileName = str(current_file_name) + "_result" + str(signedint_to_alphabetString(int(i))) + str(j) + ".png"
    print("Save image", saveFileName)
    result.save(saveFileName)

inputImageName = raw_input("Input File Name include extension. ex) image.png\n")
inputImage = Image.open(inputImageName)
print("image size is ", str(inputImage.size[0]),"x", str(inputImage.size[1]))

print("background initializing value input (void to set white)")
bg_color = raw_input("[ex : input type : ff00ff or green or (255,0,255,120)]\n#NOTE : NOT ALLOWED WITHOUT BRACELET comma phrase (EX : \"0,1,0\")\n")
if(bg_color==""):
    pass
else:
    if(bg_color.startswith("#")):
        bg_color=bg_color[1:9]
        

print("Devide image with NxM (with N columns, M rows)")
print("input N in integer")
n = int(input())
print("input M in integer")
m = int(input())

'''
if n >= 10 or m >= 10:
    print("NOTICE!! I recommend n and m would be smaller than 10 due to file name system")
'''

mode = int(raw_input("Mode Selection\n0 : Block (Side face)\n1 : Flat (Side face)\n2 : Block (Upper face)\n3 : floor panel (Upper face)\nYour Choose > "))

w = inputImage.size[0]/n
h = inputImage.size[1]/m
if w > h:
    w = h
    print(100 - w*n*100/inputImage.size[0], "% lost for width")
else:
    h = w
    print(100 - h*m*100/inputImage.size[1], "% lost for height")

tmpImage = inputImage.crop((0,0,w*n,h*m))
tmpImage.save(inputImageName[:inputImageName.rfind(".")][inputImageName.replace("../", "   ").replace("./","  ").rfind("/") + 1:] + "_result.png")

for i in range(n):
    for j in range(m):
        imageProcessor(inputImage, j, i, n, m, mode, bg_color)

raw_input ("Press Enter to Continue...")
