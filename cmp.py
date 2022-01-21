#JDI (JDIRSMV)
from PIL import Image
import sys
import os

def cEngine(file, fileN):
    image = Image.open(file)
    image.save('C://Users//{}//Pictures//Comprimidos//{}.jpeg'.format(os.getlogin(), os.path.splitext(fileN)[0]), 'jpeg', optimize = True, quality = 10)
    print('{} comprimido en > C://Users//{}//Pictures//Comprimidos'.format(fileN, os.getlogin()))

if not(os.path.isdir('C://Users//{}//Pictures//Comprimidos'.format(os.getlogin()))):
    os.mkdir('C://Users//{}//Pictures//Comprimidos'.format(os.getlogin()))

if(len(sys.argv) > 1):
    if(os.path.isdir(sys.argv[1])):
        for file in os.listdir(sys.argv[1]):
            if(os.path.splitext(file)[1].lower() in ['.jpg', '.jpeg'] and not 'compressed_' in os.path.splitext(file)[0]):
                cEngine(sys.argv[1] + '//' + file, file)