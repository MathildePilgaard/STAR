import  os #Package used to read file names in folder
import  glob #Package used to list files in Python
import  sys
import  traceback
from pathlib import Path

# 1) Kode der henter og læser alle filer under mappen "J:\VOA" og samtlige undermapper. 
# Hvis med mellemrum tilføj r foran path:

path = r'J:\VOA\4Studenterbulen\SAS nyttige koder'

#Tjek om VOA-path eksiterer:
out = os.path.isfile('J:\VOA\exception_print_opholdsgrundlag_mangler_mapning.xlsx')
print(out)

# 2) Loop der printer alle filer i mappe og undermapper:

list_files = []
for root, dirs, files in os.walk(path):
    for file in files:
        print(file)
        list_files.append(os.path.join(root,file))
for name in list_files:
	print(name)
 
os.chdir(path)

#3) Læs filer:
def read_files(file_path):
    with open(file_path, 'r') as file:
        print(file.read())



    