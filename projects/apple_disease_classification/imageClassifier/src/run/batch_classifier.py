import random
import os 
import shutil

source = 'path'
dest = 'path'
files = os.listdir(source)
k = 80          # Aantal bestanden, in dit geval 'batch size'.


for file_name in random.sample(files, k):
    shutil.[COPY OR MOVE](os.path.join(source, file_name), dest) # kies tussen 'copy' en 'move'.