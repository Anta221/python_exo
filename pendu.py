#"exo non terminé"
import random

random_word = random.choice(['aigle','buse','faucon','milan'])
print(random_word)

alphabet = []
essai = len (random_word)
user_choice = input('Faites votre choix : ')
letter=''
for i in enumerate(random_word):
    letter = i
    print (letter)

    if user_choice == letter :
        print(i , 'lettre correcte')
        print('score est de ', essai)
        user_choice = input('Faites votre choix : ')
             
    else :
        print('lettre incorrecte')
        essai = essai-1
        if essai == 0:
         print('vous avez perdu')
         break;
        else:
            print('score est de ', essai)
            user_choice = input('Faites votre choix : ')
            



    