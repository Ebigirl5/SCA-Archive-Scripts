#eSCAN_titlechange_searchPDF.py
#search in pdf for date and update file untitled_folder
#useful site: https://medium.com/analytics-vidhya/how-to-extract-texts-from-pdf-file-and-search-keywords-from-extracted-text-in-python-c5f3d4841f20

#library to search in a pdf
import PyPDF2

# Python program to rename all file names in your directory
import os

# note the file directory will be Desktop if on Desktop, but is Volumes if on thumbdrive
# make sure this python code is saved/stored in the conversion folder so that it can read the files in the folder
inp = input('Enter folder path:')
#if len(inp) < 1: inp = '/Volumes/ESCAN/Elise-data/conversion_folder'
if len(inp) < 1: inp = '/Users/elisemartin/Desktop/SCA-Archive_Python/eSCAN-code-and-samples'
os.chdir(str(inp))
print("path:", os.getcwd())        #prints current working directory path

for f in os.listdir():              #for loop works through each file in folder
    f_name, f_ext = os.path.splitext(f) #pull extension and save as f_ext
    if ".pdf" not in f_ext : continue #skip non-pdf files
    if f.startswith('.') : continue #skip weird files
    if "code" in f : continue #skip code pdf

    #open and search in pdf
    pdfFileObj = open(f, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #print(pdfReader.numPages) # will give total number of pages in pdf

    #extract all text from page 1, will get page coding
    pageObj = pdfReader.getPage(0)
    #then will show the actual texts
    text=(pageObj.extractText())
    text=text.split(",")

    print("FILE NAME:", f_name)
    print("text0:", text[0])
    print("text1:", text[1])

    if "eSCAN" not in str(text[0]):                    #skip non-eSCAN files
        print("***NOT eSCAN File:", f_name)
        continue

    try:
        header1 = text[0]             #month & day
        jumble1 = header1.split()
        length1 = len(jumble1)
        print("JUMBLE1:", jumble1)
    except:
        jumble1 = "x"
        length1 = 0

    try:
        header2 = text[1]             #year
        jumble2 = header2.split()
        length2 = len(jumble2)
        print("JUMBLE2:", jumble2)
    except:
        jumble2 = "y"
        length2 = 0

    try:
        header3 = text[2]             #alternate month & day
        jumble3 = header3.split()
        length3 = len(jumble3)
        print("JUMBLE3:", jumble3)
    except:
        jumble3 = "z"
        length3 = 0

    try:
        header4 = text[3]             #alternate year
        jumble4 = header4.split()
        length4 = len(jumble4)
        print("JUMBLE4:", jumble4)
    except:
        jumble4 = "q"
        length4 = 0

    try:                                   #turning month into number value
        monthWord = jumble1[length1 - 2]
    except:
        monthWord = "Null"
    pie = 1
    if monthWord == "January":
        month = "01"
    elif monthWord == "February":
        month = "02"
    elif monthWord == "March":
        month = "03"
    elif monthWord == "April":
        month = "04"
    elif monthWord == "May":
        month = "05"
    elif monthWord == "June":
        month = "06"
    elif monthWord == "July":
        month = "07"
    elif monthWord == "August":
        month = "08"
    elif monthWord == "September":
        month = "09"
    elif monthWord == "October":
        month = "10"
    elif monthWord == "November":
        month = "11"
    elif monthWord == "December":
        month = "12"
    else:
        try:
            monthWord = jumble2[length2 - 2]
        except:
            monthWord = "Null"
        pie = 2
        if monthWord == "January":
            month = "01"
        elif monthWord == "February":
            month = "02"
        elif monthWord == "March":
            month = "03"
        elif monthWord == "April":
            month = "04"
        elif monthWord == "May":
            month = "05"
        elif monthWord == "June":
            month = "06"
        elif monthWord == "July":
            month = "07"
        elif monthWord == "August":
            month = "08"
        elif monthWord == "September":
            month = "09"
        elif monthWord == "October":
            month = "10"
        elif monthWord == "November":
            month = "11"
        elif monthWord == "December":
            month = "12"
        else:
            monthWord = jumble3[length3 - 2]
            pie = 3
            if monthWord == "January":
                month = "01"
            elif monthWord == "February":
                month = "02"
            elif monthWord == "March":
                month = "03"
            elif monthWord == "April":
                month = "04"
            elif monthWord == "May":
                month = "05"
            elif monthWord == "June":
                month = "06"
            elif monthWord == "July":
                month = "07"
            elif monthWord == "August":
                month = "08"
            elif monthWord == "September":
                month = "09"
            elif monthWord == "October":
                month = "10"
            elif monthWord == "November":
                month = "11"
            elif monthWord == "December":
                month = "12"

    if pie == 1:
        day = str(jumble1[length1 - 1])
        year = str(jumble2[0])
    elif pie == 2:
        day = str(jumble2[length2 - 1])
        year = str(jumble3[0])
    elif pie == 3:
        day = str(jumble3[length3 - 1])
        year = str(jumble4[0])

    print("monthWord:", monthWord)
    print("day:", day)
    print("year:", year)

    name = "eSCAN_"
    new_name = name + year + "-" + month + "-" + day + f_ext
    print("new name:", new_name)
    os.rename(f, new_name)
