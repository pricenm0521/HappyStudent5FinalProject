# functions.py
# Name: Nicole Price, Zavier DePillo, Mariangel Betancourt
# email: pricenm@mail.uc.edu, depillzj@mail.uc.edu, betancmg@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Use of 2 functions to decrypt a JSON File and print the decode location of a statue, then present the picture of our group there
# Citations: 
# Anything else that's relevant: Group project

import json
from PIL import Image, ImageFilter, ImageDraw, ImageFont


def decryptLocationData(filePath, key):
    # load the encrypted data from the file
    with open(filePath) as f:
        encryptedData = json.load(f)
    # get the list of encrypted indices 
    encryptedList = encryptedData[key]
    # read the text file and extract the decrypted string
    with open('english.txt') as f:
        textFile = f.readlines()
    decryptedStr = ''
    for index in encryptedList:
        decryptedStr += textFile[int(index)-1].strip() + ' '
    # return the decrypted location
    return decryptedStr.strip()


def show_image(imagePath) :
    myimage = Image.open(imagePath)
    myimage.show()

