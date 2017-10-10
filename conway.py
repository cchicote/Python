#! python2.7.13
# conway.py

from __future__ import print_function
from Tkinter import *
import logging, os, sys, random, time
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

x_max = 20
y_max = 20
#fen1 = Tk()
#can1 = Canvas(fen1, bg='dark grey', width = x_max, height = y_max)
#can1.pack()

class Case():
    def __init__(self):
        self.state = False
        self.next_state = False

def create_tab():
    if (x_max < 10 or y_max < 10):
        raise Exception("Taille de tableau insuffisante")
    tab = []
    for x in range(x_max):
        sub = []
        for y in range(y_max):
            sub.append(Case())
        tab.append(sub)
    return (tab)

def print_tab(tab):
    for x in range(x_max):
        for y in range(y_max):
            if (tab[x][y].state == False):
                print(".", end='')
            else:
                print("O", end='')
            print(' ', end='')
        print('')
    print('\n\n\n')

def check_cell(tab, x, y):
    cells = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((x + i) >= 0 and (y + j) >= 0 and (x + i) < x_max and (y + j) < y_max):
                if (tab[x + i][y + j].state == True):
                    cells += 1
    if (tab[x][y].state == True and (cells == 3 or cells == 4)):
        tab[x][y].next_state = True
    elif (tab[x][y].state == False and cells == 3):
        tab[x][y].next_state = True
    else:
        tab[x][y].next_state = False

def life(tab):
    # On parcourt le tableau a 2 dimensions et on assigne l'etat suivant de chaque cellule
    for x in range(x_max):
        for y in range(y_max):
            check_cell(tab, x, y)
    # On change l'etat actuel par la valeur de next_state
    for x in range(x_max):
        for y in range(y_max):
            tab[x][y].state = tab[x][y].next_state
            tab[x][y].next_state = False

def draw_tab(tab):
    can1.delete(can1)
    for x in range(x_max):
        for y in range(y_max):
            if (tab[x][y].state == True):
                can1.create_line(x, y, x + 1, y, fill="blue")
                mainloop()

    
def main():
    tab = create_tab()
    tab[10][5].state = True
    tab[10][6].state = True
    tab[10][7].state = True
    tab[10][8].state = True
    tab[10][9].state = True
    tab[10][10].state = True
    tab[10][11].state = True
    tab[10][12].state = True
    tab[10][13].state = True
    tab[10][14].state = True
    print_tab(tab)
    #draw_tab(tab)
    while True:
        #time.sleep(1)
        life(tab)
        print_tab(tab)
        #draw_tab(tab)
        #can1.pack()
    

try:
    main()
except Exception as err:
    print("An exception happened: " + str(err))

#os.system("pause")
logging.debug('End of program')
