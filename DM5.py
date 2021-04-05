#########################################################
#          DM5 : matrice de score d'alignement          # 
#########################################################

#Introduction DM 5
import time
print("Bienvenue dans notre programme!!!")
time.sleep (1)
print("Celui-ci permettra de calculer les coûts d\'alignement des séquences nucléotidiques de votre choix.")
print("Il affichera le résultat sous forme d'une matrice.")
time.sleep (2)
print("\nLes paramètres de mismatch, gap, et score d'identité seront fixés par l'utilisateur.\n")
time.sleep(3)
# ====================================================================================================================
## Fonction validant la séquence entrée
def valide(seq) : 
    for base in seq : # Pour chaque base de la séquence
        if not (base in "ATCGagct") : # Si la lettre de correspond pas à la liste de lettres données
            print("La séquence suivante :",sequence," n'est pas valide.") # Affichage erreur
            seq = input("Veillez entrer une séquence correcte : ") # Demande d'entrée une nouvelle séquence
    seq = seq.upper() # Mettre la séquence en majuscule
    return(seq) # Retourne la séquence 
# ====================================================================================================================
## Fonction créant la matrice
def creationMatrice (nbL, nbC, seq1, seq2) : # nbL : nombre de lignes, nbC : nombre de colonnes
    MAT = [[0.0] * (nbC) for _ in range (nbL)] # Création de la matrice
    for j in range(2,nbC) : # Ajout séquence2 sur ligne 0
        MAT[0][j]=seq1[j-2]
    for i in range(2,nbL) : # Ajout séquence1 sur colonne 0
        MAT[i][0]=seq2[i-2]
    for j in range(2,nbC) : # Initialisation des gap sur la ligne
        MAT[1][j]=(MAT[1][j-1]+gap)
    for i in range(2,nbL) : # Initialisation des gap sur la colonne
        MAT[i][1]=(MAT[i-1][1]+gap)
    return (MAT) # Retourne la matrice
# ====================================================================================================================
## Fonction remplissant la matrice
def remplissageMatrice(nbL, nbC, MAT) : 
    for i in range (2,nbL) : # 
        for j in range (2,nbC) :
            a = MAT[i][j-1] + gap # Gap colonne
            b = MAT[i-1][j] + gap # Gap ligne
            if(MAT[i][0] == MAT[0][j]) : # Si les nucléotides sont égales 
                c = MAT[i-1][j-1] + identite # Ajout du score identité à la valeur de la diagonale en haut à gauche
            else : # Sinon
                c = MAT[i-1][j-1] + mismatch # Ajout du score mismatch à la valeur de la diagonale en haut à gauche
            MAT[i][j]= min(a, b, c) # La cellule à remplir garde seulement la valeur minimale des 3
    return (MAT) # Retoune la matrice remplie
# =====================================================================================================================
## Fonction affichant la matrice 
def affichageMatrice (MAT, nbL) :
    for j in range(nbL):
        print(matrice[j]) # Affiche matrice ligne par ligne
        
##########################################
#                   main                 #
########################################## 

# Déclaration de variables
# Entrée des scores gap, identité et mismatch 
gap = float(input("Entrer le score gap : "))
identite = float(input("Entrer le score d'identite : "))
mismatch = float(input("Entrer le score mismatch : "))
# Entrée et vérification des séquences
sequence1 = input("Entrer la première séquence : ")
sequence1 = valide(sequence1)
sequence2 = input("Entrer la deuxième séquence : ")
sequence2 = valide(sequence2)
# +2 pour éviter le chevauchement des 2 séquences 
colonnes = len(sequence1)+2
lignes = len(sequence2)+2
# Création, remplissage et affichage de la matrice
matrice = creationMatrice(lignes, colonnes, sequence1, sequence2)
matrice = remplissageMatrice(lignes, colonnes, matrice)
affichageMatrice(matrice, lignes)
