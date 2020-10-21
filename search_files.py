import shutil, os
import re

saftRegex = re.compile(r"^\d\d\d\d\d ?-? ?S?A?F?T? ? ? ?09-2020 ? ?.pdf")

string_files = ""
for foldername, subfolders, filenames in os.walk(r"C:\Users\Frede\OneDrive\Ambiente de Trabalho\documentos_trabalho"):
    for filename in filenames:
        #print('FILE INSIDE ' + foldername + ': '+ filename)
        if re.findall(saftRegex, filename.strip()):
            string_files += filename +"\n"
            try:
                shutil.copy(foldername +"\\" + filename, "saft_09_2020")
            except shutil.SameFileError:
                pass


print(string_files)