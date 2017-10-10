from PySide import QtGui, QtCore
import sys
import os


class Fenetre(QtGui.QMainWindow):
    def __init__(self):
        super(Fenetre, self).__init__()
        self.createInterface()
        self.show()

# Fonction qui permet de renommer les fichiers
    def renommer(self):
        self.noms = os.listdir(os.getcwd())
        error = 0
        if (self.input_num.text() and self.input_name.text()):
            numero = int(self.input_num.text())
            nom = self.input_name.text()
            if (numero >= 0 and numero < len(self.noms)):
                i = 0
                if (nom == self.noms[numero]):
                    error += 1
                    print("ERREUR - le fichier porte deja ce nom")
                while (i < len(self.noms)):
                    if (nom == self.noms[i]):
                        error += 1
                        if (error == 1):
                            print("ERREUR - ce nom est deja utilise par un" +
                                  " autre fichier")
                    i += 1
                if (error == 0):
                    os.rename(self.noms[numero], nom)
                    self.elem_list[numero].setText(str(numero) + " " + nom)
                    print("SUCCESS!")
            else:
                error += 1
                print("ERREUR - Saisissez un numero valide")
        else:
            error += 1
            print("ERREUR - Entrez un numero de fichier valide ainsi qu'un" +
                  " nom de fichier valide")

    def createInterface(self):
        # Gestion du background
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), 0xffffff)
        self.setPalette(self.p)

# Gestion de l'aspect general
        self.noms = os.listdir(os.getcwd())
        self.resize(500, 200 + 20 * len(self.noms))
        self.setFont(QtGui.QFont("Verdana"))
        self.setWindowTitle("Renommer un fichier")

# Bouton 1
        rename = QtGui.QPushButton("OK", self)
        rename.setGeometry(380, 80, 40, 30)
# On appelle la fonction "renommer" quand on click sur le bouton
        rename.clicked.connect(self.renommer)

# Input du numero de fichier
        self.input_num = QtGui.QLineEdit("", self)
        self.input_num.setGeometry(300, 80, 40, 30)

# Input du nom de fichier
        self.input_name = QtGui.QLineEdit("", self)
        self.input_name.setGeometry(300, 120, 120, 30)

# On appelle la fonction createList
        self.createList()

# Fonction qui permet d'initialiser la liste de fichiers
    def createList(self):
        i = 0
        self.elem_list = []
        while (i < len(self.noms)):
            self.elem_list.append(QtGui.QLabel(str(i) + " " + self.noms[i],
                                               self))
            self.elem_list[i].setGeometry(50, 80 + i * 20, 220, 30)
            i += 1

app = QtGui.QApplication(sys.argv)
frame = Fenetre()
sys.exit(app.exec_())
