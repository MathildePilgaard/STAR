import  os #Package used to read file names in folder
import  glob #Package used to list files in Python
import  sys
import  traceback
from pathlib import Path

message = 'hello Mathilde you got this'
print(message)

#Kode der henter og læser alle filer under mappen "J:\VOA" og samtlige undermapper:
#File_object = open(r"path","Access_Mode") Ved ikke om jeg skal bruge denne i stedet...?
#Alternativ med python3: data_folder = Path("source_data/text_files/")

path = r'J:\\VOA'

#Tjek om path eksiterer:
out = os.path.isfile("J:\\VOA")

print(out)

list_files = []
for root, dirs, files in os.walk(path):
	for file in files:
		list_files.append(os.path.join(root,file))
for name in list_files:
    print(name)



    