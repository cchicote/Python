#! python2.7.13
# bot.py
# THIS PROJECT GOT CANCELED

from __future__ import print_function
from Tkinter import *
import logging, pyautogui, time, random
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

def donnees():
    coords = {'Mine Hable':
          {'map0':
           [{'ressources':
             {'fer': [[505, 609], [553, 582], [908, 144], [954, 117]]}},
            {'acces':
             {'entree': [541, 853], 'sortie': [1402, 231], 'point blanc': [575, 712]}}],

           'map1':
           [{'ressources':
             {'fer': [[778, 121], [825, 138], [1365, 341], [1543, 431]],
              'cuivre': [[610, 676], [1048, 358], [1090, 346]]}},
            {'acces':
             {'entree': [601, 910],
              'sortie': [1490, 496],
              'point blanc': [1009, 416]}}],
           'map2':
           [{'ressources':
             {'fer': [[919, 135], [1227, 452], [1438, 535], [1062, 214]],
              'cuivre': [[419, 648], [554, 593], [603, 578], [1181, 471]],
              'bronze': [[468, 644], [975, 161], [975, 456], [1496, 558]],
              'kobalte': [[660, 513]]}},
            {'acces':
             {'entree': [497, 872],
              'sortie': [1399, 581],
              'point blanc': [1026, 500]}}],
           'map3':
           [{'ressources':
             {'fer': [[482, 686], [730, 142], [790, 132], [874, 93], [910, 75]],
              'cuivre': [[1219, 289], [1397, 336], [1455, 353]],
              'bronze': [[517, 678], [604, 320], [651, 301], [1006, 102], [1044, 114]],
              'kobalte': [[763, 486]],
              'etain': [[1154, 181]]}},
            {'acces':
             {'entree': [519, 880],
              'sortie': [519, 880],
              'point blanc': [1026, 500]}}]}}
    return (coords)

# Fonction qui permet de recuperer les donnees souhaitees contenues sur la map donnee en parametre
# get_data('Mine Hable', 'map1', 'cuivre') retourne les coordonnees des filons de cuivre sur la map1 de la Mine Hable
# get_data('Mine Hable', 'map0', 'cuivre') retourne False car il n'y a pas de cuivre sur la map0 de la Mine Hable
# get_data('Mine Hable', 'map1', 'acces') retourne un dictionnaire contenant les acces de la map1 de la Mine Hable
# get_data('Mine Hable', 'map1', 'all') retourne toutes les donnees de la map1 de la Mine Hable
def get_data(coords, mine_to_dissect, map_to_dissect, data_to_get):
    if (mine_to_dissect in coords and map_to_dissect in coords[mine_to_dissect]):
        if (data_to_get == 'all'):
            return coords[mine_to_dissect][map_to_dissect]
        for map_content in coords[mine_to_dissect][map_to_dissect]:
            for content_category in map_content:
                if (data_to_get == content_category):
                    return map_content[content_category]
                if (data_to_get in map_content[content_category]):
                    return map_content[content_category][data_to_get]
        return False
    else:
        return False

# Fonction qui check si les donnees sont correctes
def check_data(ressources, entree, sortie, point_blanc):
    if (ressources == False or entree == False or sortie == False or point_blanc == False):
        raise Exception("Donnee mal mappee")

def queue_up(coordonnees):
    pyautogui.keyDown('shift')
    pyautogui.click(coordonnees)
    pyautogui.keyUp('shift')

def check_combat():
    if (pyautogui.screenshot().getpixel((1757, 891)) == (0, 0, 0)):
        return (False)
    return (True)

def combat():
    logging.debug("buff")
    pyautogui.press('3')
    time.sleep(0.5)
    pyautogui.click(1819, 877)
    time.sleep(0.5)
    for i in range(3):   
        logging.debug("attaque")
        pyautogui.press('2')
        time.sleep(0.5)
        pyautogui.click(1757, 891)
        time.sleep(1)
    logging.debug("Fin de tour")
    time.sleep(2)
    pyautogui.press('`')
    time.sleep(5)

def mask_combat():
    pyautogui.click(1336, 913)
    time.sleep(0.5)
    pyautogui.click(1348, 971)
    time.sleep(0.5)
    pyautogui.click(1322, 1017)

def prepare_combat(ressources, io):
    mask_combat()
    time.sleep(2)
    while (check_combat() == True):
        combat()
    time.sleep(2)
    logging.debug("Sortie du combat")
    pyautogui.press('enter')
    time.sleep(2)
    if (io == True):
        logging.debug("Appel take_ressources depuis prepare_combat: %s" % (ressources))
        take_ressources(ressources)
    
def take_ressources(ressources):
    logging.debug("Entree take ressources: %s" % (ressources))
    for ressource in ressources:
        for i in range(len(ressources[ressource])):
            if (check_combat() == True):
                prepare_combat(ressources, True)
            filon = ressources[ressource].pop()
            queue_up(filon)
    logging.debug("Map cleaned %s" % (ressources))

def get_out(sens, entree, sortie):
    logging.debug("Get out")
    if (sens == 1):
        queue_up(sortie)
    elif (sens ==  -1):
        queue_up(entree)

def check_lvlup():
    if (pyautogui.screenshot().getpixel((873, 472)) == (225, 248, 0)):
        logging.debug("il y a effectivement le lvlup")
        time.sleep(0.5)
        pyautogui.click(873, 472)
        return True
    return False

def room_end(point_blanc, ressources, sens, entree, sortie):
    logging.debug("Room end")
    pyautogui.moveTo(938, 472)
    logging.debug("Wait")
    while True:
        check_lvlup()
        # Check si le panneau lvlup est affiche
        if (check_combat() == True):
            logging.debug("Debut de combat, room_end")
            prepare_combat(ressources, False)
            get_out(sens, entree, sortie)
            break
        if (pyautogui.screenshot().getpixel((point_blanc[0], point_blanc[1])) == (0, 0, 0)):
            logging.debug("Salle suivante")
            pyautogui.press('enter')
            break
        
def bot_ft(mine_name, map_name, sens):
    # Assigne les valeurs
    coords = donnees()
    ressources = get_data(coords, mine_name, map_name, 'ressources')
    entree = get_data(coords, mine_name, map_name, 'entree')
    sortie = get_data(coords, mine_name, map_name, 'sortie')
    point_blanc = get_data(coords, mine_name, map_name, 'point blanc')
    
    # Check si les donnees sont correctes
    check_data(ressources, entree, sortie, point_blanc)

    # Check si le panneau lvlup est affiche
    check_lvlup()

    # Met en file d'attente toutes les ressources et gere le combat
    take_ressources(ressources)

    # Check le combat avant de passer a la salle suivante
    if (check_combat() == True):
        logging.debug("Combat 1")
        prepare_combat(ressources, False)
        
    # Met en file d'attente l'entree ou la sortie de la map selon le sens
    get_out(sens, entree, sortie)

    # Check le combat avant de passer a la salle suivante
    if (check_combat() == True):
        logging.debug("Combat 2")
        prepare_combat(ressources, False)
        get_out(sens, entree, sortie)
        
    # Gere le point blanc et enclenche la sequence suivante
    room_end(point_blanc, ressources, sens, entree, sortie)

    

def main():
    liste_mine = ['Mine Hable']
    liste_map = ['map0', 'map1', 'map2', 'map3']
    while True:
        for i in range(0, len(liste_map) - 1, 1):
            bot_ft(liste_mine[0], liste_map[i], 1)
            time.sleep(0.5)
        for i in range(len(liste_map) - 1, 0, -1):
            bot_ft(liste_mine[0], liste_map[i], -1)
            time.sleep(0.5)

def main2():
    fenetre = Tk()
    fenetre.resize(500)
    fenetre.mainloop()


try:
    main()
    #main2()
    
except Exception as err:
    print("Exception raised: " + str(err))

logging.debug('End of program')
