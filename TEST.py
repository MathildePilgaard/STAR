import  os #Package used to read file names in folder
import  glob #Package used to list files in Python
import  sys
import  traceback
from pathlib import Path
import regex
import PyPDF2
import openpyxl
import pdfplumber
import re

# 1) Kode der henter og læser alle filer under mappen "J:\VOA" og samtlige undermapper. 
# Hvis med mellemrum da tilføj r foran path:
# path = 'J:\VOA'

#Beyttes til test:
path = r'J:\VOA\4Studenterbulen'

#Tjek om VOA-path eksiterer:
#out = os.path.isfile('J:\VOA\exception_print_opholdsgrundlag_mangler_mapning.xlsx')
#print(out)

#2) Læs filer af TXT og .xls og printer sti:
def read_files(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        return file_contents
        
def check_for_cpr_numbers(file_contents):
    match = regex.search("([0-9]{6}-[0-9]{4}|^[0-9]{9,10}$)", file_contents, regex.IGNORECASE)
    #Læser nu ikke komma og punktum samt læser kun 9-10 antal hele tal.
    return True if match else False
            
list_files = []
for root, dirs, files in os.walk(path):
    print(f'Currently at {root}')
    for file in files:
        # print(file)
        if file.endswith('txt'):
            list_files.append(os.path.join(root,file))

print('Listing found files containing CPR:')
for name in list_files:
    file_contents = read_files(name)
    if check_for_cpr_numbers(file_contents) is True:
        #Er true og false med her? Jeg har tilføjet 'is True'.
        #Tilføj til ny liste der indeholder oversigt over alle filenavn der har cpr numre i sig
        #returne listen af filnavne eller printe den, eller gemme i en ny fil
        print(name)
        pass
    
#4) Læs PDF'er med cpr-nummer:
#Creating a pdf file object 
pdfpath = PyPDF2.PdfFileReader(path)

def read_files(pdffile_pdfpath):
    with open(pdffile_pdfpath, 'r') as pdffile:
        pdffile_contents = pdffile.read()
        return pdffile_contents

def check_for_cpr_numbers(pdffile_contents):
    match = regex.search("([0-9]{6}-[0-9]{4}|^[0-9]{9,10}$)", file_contents, regex.IGNORECASE)
    #Læser nu ikke komma og punktum samt læser kun 9-10 antal hele tal.
    return True if match else False

list_pdffiles = []
for root, dirs, files in os.walk(pdfpath):
    print(f'Currently at {root}')
    for file in pdffiles:
        # print(file)
        if file.endswith('pdf'):
            list_files.append(os.pdfpath.join(root,file))

print('Listing found files containing CPR:')
for name in list_files:
    file_contents = read_files(name)
    if check_for_cpr_numbers(pdffile_contents) is True:
        #Er true og false med her? Jeg har tilføjet 'is True'.
        #Tilføj til ny liste der indeholder oversigt over alle filenavn der har cpr numre i sig
        #returne listen af filnavne eller printe den, eller gemme i en ny fil
        print(name)
        pass





















