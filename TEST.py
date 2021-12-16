message = 'hello world'
print(message)

import  os #Package used to read file names in folder
import  glob #Package used to list files in Python
import  sys
import  traceback

#Kode der henter og læser alle filer under mappen "J:\VOA" og samtlige undermapper:
#File_object = open(r"path","Access_Mode")

path =r'C:\J:\VOA'
#Check om path er correct:
os.path.isdir(path)

list_files = []
for root, dirs, files in os.walk(path):
	for file in files:
		list_files.append(os.path.join(root,file))
for name in list_files:
    print(name)
    
    
    
