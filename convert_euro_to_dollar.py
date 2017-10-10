from PySide import QtGui, QtCore
import sys


class Fenetre(QtGui.QMainWindow):
    def __init__(self):
        super(Fenetre, self).__init__()
        self.createInterface()
        self.show()

    def conversion(self):
        print(self.mult)
        try:
            val = float(self.valeur.text())
        except ValueError:
            val = 0
        val = val * self.mult
        self.label.setText("{:.2f}".format(val))

    def switchq(self):
        if self.id == 0:
            self.eu_to_d()
        else:
            self.d_to_eu()
        self.conversion()

    def eu_to_d(self):
        self.right_curr.setText("euros")
        self.left_curr.setText("dollars")
        self.mult = 0.892657889
        self.id = 1
        self.p.setColor(self.backgroundRole(), 0x669933)
        self.setPalette(self.p)

    def d_to_eu(self):
        self.right_curr.setText("dollars")
        self.left_curr.setText("euros")
        self.mult = 1.12025
        self.id = 0
        self.p.setColor(self.backgroundRole(), 0x003399)
        self.setPalette(self.p)

    def createInterface(self):
        self.setAutoFillBackground(True)
        self.resize(500, 200)
        self.setFont(QtGui.QFont("Verdana"))
        self.setWindowTitle("Convertissseur Euros/Dollars - Dollars/Euro")
        self.mult = 1.12025
        self.id = 0
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), 0x003399)
        self.setPalette(self.p)

        self.valeur = QtGui.QLineEdit("", self)
        self.valeur.setGeometry(50, 55, 100, 30)

        convert = QtGui.QPushButton("Convertir", self)
        convert.setGeometry(200, 55, 100, 30)
        convert.clicked.connect(self.conversion)

        self.label = QtGui.QLabel("0.00", self)
        self.label.setGeometry(350, 55, 100, 30)

        self.left_curr = QtGui.QLabel("euros", self)
        self.left_curr.setGeometry(50, 100, 100, 30)

        switchbutton = QtGui.QPushButton("Switch", self)
        switchbutton.setGeometry(200, 100, 100, 30)
        switchbutton.clicked.connect(self.switchq)

        self.right_curr = QtGui.QLabel("dollars", self)
        self.right_curr.setGeometry(350, 100, 100, 30)

app = QtGui.QApplication(sys.argv)
frame = Fenetre()
sys.exit(app.exec_())
