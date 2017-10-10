#! python2.7.13
# voie_lactee.py
# A faire : faire en sorte qu'il n'y ait qu'un certain % de pixels d'une certaine couleur (genre pas plus de 1% de pixels orange, etc...)

from __future__ import print_function
from PIL import ImageColor, Image
import logging, os, random
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

#os.chdir("C:\\Users\\Come\\Desktop\\voie_lactee")
size = 15000
name = "voie_lactee"
new_img = Image.new('RGBA', (size, size), 'black')
colors = ['white', 'grey', 'darkgrey', 'dimgrey', 'lightgrey', 'lightslategrey', 'slategrey', 'whitesmoke', 'rosybrown']
logging.debug("Generation de l'image")
pourcent = 0
logging.debug("0%")
for i in range(size):
    for j in range(size / 100):
        new_img.putpixel((random.randint(0, size - 1), random.randint(0, size - 1)), ImageColor.getcolor(colors[random.randint(0, len(colors) - 1)], 'RGBA'))
        #new_img.paste(Image.new('RGBA', (1, 1), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))), (random.randint(0, size), random.randint(0, size)))
    tmp = int(100 * float(i) / float(size))
    if (tmp != pourcent):
        pourcent = tmp
        if (pourcent % 10 == 0):
            logging.debug(str(pourcent) + "%")
logging.debug("100%")
logging.debug("Sauvegarde de l'image")
if (os.path.exists(name + ".png")):
    i = 2
    name = name + str(i)
    while(os.path.exists(name + ".png")):
        i += 1
        if (i == 10):
            name = name[:-1]
        else:
            name = name[:-len(str(i))]
        name = name + str(i)
new_img.save(name + ".png")
logging.debug("Success")
logging.debug('End of program')
