#Le programme génère un prix rond aléatoire
#user entre le prix 
#on fait le controle pour voir si le prix est > ou < ou prix aléatoire 
#s'il fausse sont score diminue
# s'il gagne ou perd on lui redemande de jouer
#et il peut être chronométrer

import random
from math import *

prix_rond = round(random.randint(1, 10))
score = 5

print('votre score est', score)
prix_user = int(input('Entrez votre prix  : '))
start = 't'

i = 0
while i < score : 
    if start == 't':
        
        if prix_rond > prix_user  :
            print('Le prix rond est suppérieur')
            scoreRestant = score - 1
        elif prix_rond < prix_user :
            print('Le prix rond est inférieur')
            scoreRestant = score - 1
        else :
            print('Bravo vous avez gagné')
            scoreRestant = score + 1
            start = str(input('voulez vous recommencer? t/f : '))
            if start == 't':
                score = scoreRestant
                prix_user = int(input('Entrez votre prix  : '))
                prix_rond = round(random.randint(1, 10))
            else :
                break

        print('votre score restant est :', scoreRestant)
        if scoreRestant == 0  :
            print('vous avez perdu')
            start = str(input('voulez vous recommencer? t/f : '))
            if start == 't':
                score = 5
                prix_user = int(input('Entrez votre prix  : '))
            else :
                break
        else : 
            prix_user = int(input('Entrez votre prix  : '))
            score = scoreRestant 


    

    