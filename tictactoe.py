from __future__ import print_function
import re

def tutoriel():
    print("\nJeu du morpion:\nObjectif: aligner 3 signes identiques en longueur, largeur, ou diagonale")
    print("Pour jouer, il faut rentrer les \'coordonnees\' pour le signe que tu veux placer")
    print("\nCa se passe comme ca : \'top-L\' pour mettre un pion ici:")
    print("\n " + 'X' + " | " + " " + " | " + " ")
    print("---+---+---")
    print(" " + " " + " | " + " " + " | " + " ")
    print("---+---+---")
    print(" " + " " + " | " + " " + " | " + " " + "\n")
    print("Tu as donc top, mid, bot pour placer ton signe sur la bonne ligne, et L, M et R pour placer ton signe sur la bonne colonne!\n\n")

def numero_du_joueur(nombre):
    if (nombre % 2 == True):
        return (1)
    return (2)

def signe_du_joueur(numero):
    if (numero == 1):
        return ('X')
    return('O')

def print_board(board):
    print("\n " + board['top-L'] + " | " + board['top-M'] + " | " + board['top-R'])
    print("---+---+---")
    print(" " + board['mid-L'] + " | " + board['mid-M'] + " | " + board['mid-R'])
    print("---+---+---")
    print(" " + board['bot-L'] + " | " + board['bot-M'] + " | " + board['bot-R'] + "\n")

def check_move(move, board):
    pattern = re.compile(r'^(top|mid|bot)-(L|M|R)$')
    return (pattern.search(move) != None and board[move] == ' ')
        
def check_board(board):
    if ((board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X') or\
        (board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X') or\
        (board['bot-L'] == 'X' and board['bot-M'] == 'X' and board['bot-R'] == 'X') or\
        (board['top-L'] == 'X' and board['mid-L'] == 'X' and board['bot-L'] == 'X') or\
        (board['top-M'] == 'X' and board['mid-M'] == 'X' and board['bot-M'] == 'X') or\
        (board['top-R'] == 'X' and board['mid-R'] == 'X' and board['bot-R'] == 'X') or\
        (board['top-L'] == 'X' and board['mid-M'] == 'X' and board['bot-R'] == 'X') or\
        (board['top-R'] == 'X' and board['mid-M'] == 'X' and board['bot-L'] == 'X')):
        return (True)
    elif ((board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O') or\
        (board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O') or\
        (board['bot-L'] == 'O' and board['bot-M'] == 'O' and board['bot-R'] == 'O') or\
        (board['top-L'] == 'O' and board['mid-L'] == 'O' and board['bot-L'] == 'O') or\
        (board['top-M'] == 'O' and board['mid-M'] == 'O' and board['bot-M'] == 'O') or\
        (board['top-R'] == 'O' and board['mid-R'] == 'O' and board['bot-R'] == 'O') or\
        (board['top-L'] == 'O' and board['mid-M'] == 'O' and board['bot-R'] == 'O') or\
        (board['top-R'] == 'O' and board['mid-M'] == 'O' and board['bot-L'] == 'O')):
        return (True)
    else:
        return (False)

def partie():
    board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}
    joueur = []

    for i in range(1, 3):
        print("Rentre le nom du joueur " + str(i))
        joueur.append(raw_input())
    for i in range(1, 10):
        print_board(board)
        print("\n\n\nAu tour de " + joueur[numero_du_joueur(i) - 1])
        move = raw_input()
        while (check_move(move, board) == False):
            print("Erreur, reessaies")
            move = raw_input()
        board[move] = signe_du_joueur(numero_du_joueur(i))
        if (check_board(board) == True):
            print("Bravo a " + joueur[numero_du_joueur(i) - 1])
            break
    if (check_board(board) == False):
        print("\n\n\nMatch nul!")
    print_board(board)

print("Salut, tu veux le tutoriel ? Oui ou Non")
if (raw_input().lower() == "oui"):
    tutoriel()

while(True):
    partie()
    print("Vous voulez rejouer ? Oui ou Non")
    if (raw_input().lower() != "oui"):
        break
