# main.py 
# Name: Nicole Price, Zavier DePillo, Mariangel Betancourt
# email: pricenm@mail.uc.edu, depillzj@mail.uc.edu, betancmg@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Use of 2 functions to decrypt a JSON File and print the decode location of a statue, then present the picture of our group there
# Citations: 
# Anything else that's relevant: Group project

from functionsPackage.functions import *

filePath = 'EncryptedGroupHints Spring 2023 Section 001.json'
# calling the function and providing the name of the index
location = decryptLocationData(filePath, 'Larisa Latynina')
# printing the decrypted location for the picture
print(location)


show_image(r"..\functionsPackage\thumbnail_image0.jpg") 
