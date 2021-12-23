message = 'hello world'
print(message)

import  os #Package used to read file names in folder
import  glob #Package used to list files in Python
import  sys
import  traceback

#Kode der henter og læser alle filer under mappen "J:\VOA" og samtlige undermapper:
#File_object = open(r"path","Access_Mode") Ved ikke om jeg skal bruge denne i stedet...?
#path =r'C:\Users\Administrator.SHAREPOINTSKY\Desktop\Work'
path = r'J:\VOA'
list_files = []
for root, dirs, files in os.walk(path):
	for file in files:
		list_files.append(os.path.join(root,file))
for name in list_files:
    print(name)