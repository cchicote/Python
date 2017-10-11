#! python2.7.13
# conway.py

from __future__ import print_function
from Tkinter import *
import logging, os, sys, random, time, functools
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

# Taille de la grille (x, y)
x_max = 35
y_max = 35
# Declencheur des sequences
running = False

# Classe correspondant a une case dans la grille
class Case():
    def __init__(self):
        self.state = False
        self.next_state = False

# Classe dans laquelle je mets toutes les variables (Comme si elles etaient set en global en fait)
class Variables():
    def __init__(self):
        self.fen1 = Tk()
        self.can1 = Canvas(self.fen1, bg='white', width = x_max * 10, height = y_max * 10)
        self.can1.pack()
        self.button_tab = []
        self.tab = []
        self.speed = 500
        self.scale = 100

# Variable globale dans laquelle on a toutes les autres variables interessantes
var = Variables()

# Cree un tableau vide de x_max par y_max
def create_tab():
    if (x_max < 10 or y_max < 10):
        raise Exception("Taille de tableau insuffisante")
    tab = []
    for x in range(x_max):
        sub = []
        for y in range(y_max):
            sub.append(Case())
        tab.append(sub)
    var.tab = tab

# Print le tableau dans le terminal
def print_tab():
    for x in range(x_max):
        for y in range(y_max):
            if (var.tab[x][y].state == False):
                print(".", end='')
            else:
                print("O", end='')
            print(' ', end='')
        print('')
    print('\n\n\n')

# Fonction qui determine si une cellule sera vivante ou morte au tour suivant selon les regles etablies par Conway
def check_cell(x, y):
    cells = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((x + i) >= 0 and (y + j) >= 0 and (x + i) < x_max and (y + j) < y_max):
                if (var.tab[x + i][y + j].state == True):
                    cells += 1
    if (var.tab[x][y].state == True and (cells == 3 or cells == 4)):
        var.tab[x][y].next_state = True
    elif (var.tab[x][y].state == False and cells == 3):
        var.tab[x][y].next_state = True
    else:
        var.tab[x][y].next_state = False

# Fonction qui assigne l'etat vivant (True) ou mort (False) aux cellules
def life():
    # On parcourt le tableau a 2 dimensions et on assigne l'etat suivant de chaque cellule
    for x in range(x_max):
        for y in range(y_max):
            check_cell(x, y)
    # On change l'etat actuel par la valeur de next_state
    for x in range(x_max):
        for y in range(y_max):
            var.tab[x][y].state = var.tab[x][y].next_state
            var.tab[x][y].next_state = False

# Fonction qui initialise puis demarre la boucle de dessin
def dessin():
    var.fen1.bind("<Button-1>", change_button_color)
    draw_grid()
    create_interface()
    draw_tab()
    scanning()
    var.fen1.mainloop()
    #canvas.grid(row=10, column=10, rowspan=3, padx=10, pady=5)
    #launch(tab, canvas, button_tab)

# On reassigne une valeur a toutes les cases de la grille
def draw_tab():
    for x in range(x_max):
        for y in range(y_max):
            if (var.tab[x][y].state == True):
                var.button_tab[x][y].config(bg="blue")
            else:
                var.button_tab[x][y].config(bg="white")

# On genere la grille
def draw_grid():
    button_tab = []
    for x in range(0, x_max):
        button_subtab = []
        for y in range(0, y_max):
            tmp = Button(var.can1, text="", width=2, height=1, command=None, relief=GROOVE, bg="white")
            tmp.grid(row= x, column = y)
            tmp.grid_propagate(False)
            button_subtab.append(tmp)
        button_tab.append(button_subtab)
    var.button_tab = button_tab

# Fonction qui permet d'interagir directement sur la grille avec la souris
def change_button_color(event):
    grid_info = event.widget.grid_info()
    try:
        x = int(grid_info["row"])
        y = int(grid_info["column"])
    except:
        return
    if var.tab[x][y].state == False:
        var.tab[x][y].state = True
        var.button_tab[x][y].config(bg="blue")
    elif var.tab[x][y].state == True:
        var.tab[x][y].state = False
        var.button_tab[x][y].config(bg="white")

#Fonctions annexes (demarrage, pause, clear, etc...)
def launch():
    #logging.debug("On parcourt bien la boucle")
    life()
    draw_tab()

def start():
    logging.debug("Start")
    global running
    if (running == True):
        return
    running = True
    var.button_start.config(bg = 'green')
    var.button_pause.config(bg = 'white')

def pause():
    logging.debug("Pause")
    global running
    if (running == False):
        return
    var.button_pause.config(bg = 'yellow')
    var.button_start.config(bg = 'white')
    running = False

def scanning():
    #logging.debug("Scanning")
    if running:
        launch()
    var.fen1.after(var.speed, scanning)

def speedup():
    logging.debug(var.speed)
    if (var.speed > 10):
        var.speed -= 10

def speeddown():
    logging.debug(var.speed)
    if (var.speed < 5000):
        var.speed += 10

def clear():
    if running:
        return
    create_tab()
    draw_grid()

# Fonction qui met en place l'interface qui entoure la grille
def create_interface():
    var.button_start = Button(var.fen1, text="Start", command=start)
    var.button_start.pack(side=RIGHT)
    var.button_pause = Button(var.fen1, text="Pause", command=pause)
    var.button_pause.pack(side=RIGHT)
    var.button_clear = Button(var.fen1, text="Clear", command=clear)
    var.button_clear.pack(side=RIGHT)
    var.button_stop = Button(var.fen1, text="Stop", command=sys.exit)
    var.button_stop.pack(side=RIGHT)
    var.button_speedup = Button(var.fen1, text="Speed UP", command=speedup)
    var.button_speedup.pack(side=LEFT)
    var.button_speeddown = Button(var.fen1, text="Speed DOWN", command=speeddown)
    var.button_speeddown.pack(side=LEFT)

def main():
    # Creation des cellules
    create_tab()
    # Affichage des cellules avec la bibliotheque Tkinter
    dessin()

try:
    main()
except Exception as err:
    print("An exception happened: " + str(err))

#os.system("pause")
logging.debug('End of program')
