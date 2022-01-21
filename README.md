### Este programa comprime las imagenes reduciendo su tamaño tratando de no perder calidad de imagen
> No siempre se puede mantener la resolucion original

###### Libreria necesaria

```cmd
pip install pillow 
```

###### Ejemplo de uso (El programa se ejecuta a base de argumentos)
> cmp.py [ruta de el archivo o carpeta] (Solo funciona con archivos `jpg` o `jpeg`)

```
cmp.py C:/Users/JDI/Pictures
```
```
cmp.py C:/Users/JDI/Pictures/image.jpg
```

###### Codigo

```python
from PIL import Image
import sys
import os

def cEngine(file, fileN):
    image = Image.open(file)
    image.save('C://Users//{}//Pictures//Comprimidos//{}_compressed.jpeg'.format(os.getlogin(), os.path.splitext(fileN)[0]), 'jpeg', optimize = True, quality = 10)
    print('{} comprimido en > C://Users//{}//Pictures//Comprimidos'.format(fileN, os.getlogin()))

if not(os.path.isdir('C://Users//{}//Pictures//Comprimidos'.format(os.getlogin()))):
    os.mkdir('C://Users//{}//Pictures//Comprimidos'.format(os.getlogin()))

if(len(sys.argv) > 1):
    if(os.path.isdir(sys.argv[1])):
        for file in os.listdir(sys.argv[1]):
            if(os.path.splitext(file)[1].lower() in ['.jpg', '.jpeg'] and not '_compressed' in os.path.splitext(file)[0]):
                cEngine(sys.argv[1] + '//' + file, file)
    elif(os.path.isfile(sys.argv[1]) and not '_compressed' in sys.argv[1] and os.path.splitext(sys.argv[1])[1] in ['.jpg', '.jpeg']):
        cEngine(sys.argv[1], os.path.splitext(os.path.basename(sys.argv[1]))[0])
else:
    print('Necesita proporcionar la ruta de el archivo(s)')
```
