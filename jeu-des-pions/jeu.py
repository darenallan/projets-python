import random

# Créer un nouveau tableau de jeu
def newBoard(n, p):
    board = []
    for i in range(n):
        nbPieces = random.randint(0, p)
        board.append(nbPieces)
    return board

#Afficher le tableaude jeu
def display(board, n):
    bordure = "----" * n + "-"
    
    print("\n" + bordure)
    
    print("|", end=" ")
    for i in range(n):
        print(board[i], end=" | ")
    print() 

    print(bordure)

    print("|", end=" ")
    for i in range(n):
        print(i + 1, end=" | ")
    print("\n" + bordure)
# Vérifier case de départ
def possibleSquare(board, n, i):
    if i <= 1 or i > n:
        return False
    if board[i - 1] <= 0:
        return False
    return True

# Sélectionner la case de départ
def selectSquare(board, n):
    while True:
        i = int(input("Entrez la case de départ : "))
        if possibleSquare(board, n, i):
            return i
        else:
            print("Impossible de choisir cette case.")

# Pour Vérifier la  case de destination
def possibleDestination(board, n, i, j):
    if j < 1 or j > n:
        return False
    if j >= i:
        return False
    return True

# Sélectionner la case de destination
def selectDestination(board, n, i):
    while True:
        j = int(input("Entrez la case destination : "))
        if possibleDestination(board, n, i, j):
            return j
        else:
            print("Destination invalide.")

# Pour verifier les deplacements
def move(board, i, j):
    board[i - 1] -= 1
    board[j - 1] += 1

# Vérifier si perdu
def lose(board, n):
    for i in range(1, n):
        if board[i] > 0:
            return False
    return True

#Demander le nom du joueur
def NomJoueur(joueur):
    nom = input("Entrez le nom du joueur : ")
    return nom

# Fonction principale
def jouerUnePartie(n,p,nomJoueur1,nomJoueur2):

    board = newBoard(n, p)
    joueur = nomJoueur1
    jouer = True

    while jouer:
        display(board, n)

        print("Tour du joueur", joueur)

        i = selectSquare(board, n)
        j = selectDestination(board, n, i)

        move(board, i, j)

        if lose(board, n):
            jouer = False
        else:
            if joueur == nomJoueur1:
                joueur = nomJoueur2
            else:
                joueur = nomJoueur1

    print("Le gagnant est le joueur", joueur)


n = int(input("Entrez le nombre de cases: "))
p = int(input("Entrez le nombre de pions par case: "))
nomJoueur1 = NomJoueur(1)
nomJoueur2 = NomJoueur(2)
jouerUnePartie(n, p, nomJoueur1, nomJoueur2)
