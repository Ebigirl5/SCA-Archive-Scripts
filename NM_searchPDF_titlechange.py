
# right now this file can open a folder containing pdfs within the same folder where this code is stored and print the text (even OCR)
#library to search in a pdf
import PyPDF2

# Python program to rename all file names in your directory
import os

# import regular expressions library
import re

import fnmatch

inp = input('Enter folder path:')
# note the file directory will be Users/'myusername'/Desktop if on Desktop, but is Volumes if on thumbdrive
# make sure this python code is saved/stored in the conversion folder so that it can read the files in the folder
if len(inp) < 1: inp = '/Users/elisemartin/Desktop/SCA-Archive_Python/NM-code-and-samples'
# if len(inp) < 1: inp = '/Volumes/CF-RED2019/SCA-arch-elise-SCAN-2021-22/SCAN-need-rename_20211205/conversion_folder'
os.chdir(str(inp))
print("path:", os.getcwd()) #prints current working directory path

for f in os.listdir():
    #if "eSCAN" not in f: continue #skip non eSCAN files
    f_name, f_ext = os.path.splitext(f) #pull extension and save as f_ext
    if ".pdf" not in f_ext : continue #skip non-pdf files
    if f.startswith('.') : continue #skip weird files
    if "code" in f : continue #skip code pdf

    print("___old name:", f)  #current file name

    #open and search in pdf
    pdfFileObj = open(f, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #print(pdfReader.numPages) # will give total number of pages in pdf

    #extract all text from page 1, will get page coding
    pageObj = pdfReader.getPage(0)
    #then will show the actual texts
    text=(pageObj.extractText())
    text=text.split(",")

    first_10_lines = str(text[:10])    #reduce number of lines to read and convert to bytes (str)

    # if text.find("1977") >= 0:                 #non-regex method

    year_list = re.findall('(19[789]\d|20[01]\d)[^0-9]', first_10_lines)        # creates list of years found
    print('*** years found:', year_list)
    year = input('ENTER YEAR, type skip to skip, break to exit: ')                                                # asks you to choose year from list
    if year == "skip":
        continue
    if year == "break":
        break

    print(first_10_lines)
    print('\n')

    month = "month not recognized"
    while month == "month not recognized":
        ask_m = input('ENTER MONTH (lower case) or 00 if unknown, type skip to skip, break to exit: ')

        try:
            if ask_m == "00":
                month = "00"
            elif ask_m == "january":
                month = "01"
            elif ask_m == "february":
                month = "02"
            elif ask_m == "march":
                month = "03"
            elif ask_m == "april":
                month = "04"
            elif ask_m == "may":
                month = "05"
            elif ask_m == "june":
                month = "06"
            elif ask_m == "july":
                month = "07"
            elif ask_m == "august":
                month = "08"
            elif ask_m == "september":
                month = "09"
            elif ask_m == "october":
                month = "10"
            elif ask_m == "november":
                month = "11"
            elif ask_m == "december":
                month = "12"
            elif ask_m == "skip" or "break":
                break
            #print("month saved as:", month)
        except:
            month = "month not recognized"
            print("error, try again")

    if ask_m == "skip":
        continue
    if ask_m == "break":
        break

    day = input('ENTER DAY (two digits, ex. 02 or 00 if unknown), type skip to skip, break to exit: ')
    if day == "skip":
        continue
    if day == "break":
        break

    new_name_no_ext = 'NM_' + year + "-" + month + "-" + day   #here year is a string
    newname_w_ext = 'NM_' + year + "-" + month + "-" + day + f_ext

    if newname_w_ext in os.listdir():
        print(fnmatch.filter(os.listdir('.'), new_name_no_ext + '*' + '.pdf'))
        print(len(fnmatch.filter(os.listdir('.'), new_name_no_ext + '*' + '.pdf')), 'copies (including this file)')
        suffix = input("choose suffix:")
        new_name = 'NM_' + year + "-" + month + "-" + day + suffix + f_ext
    else:
        new_name = 'NM_' + year + "-" + month + "-" + day + f_ext

    try:
        os.rename(f, new_name)    #os.rename(file, destination)
        print('*** new name: ', new_name)
        print('\n')
    except:
        print("========ERROR WHILE RENAMING======", f)

    # except:
    #     print('xxx unable to rename file:', f)
