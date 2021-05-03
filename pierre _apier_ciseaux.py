import random

random_choice = random.choice(['pi', 'pa', 'ci'])
user_choice = input('Fais ton choix entre Pierre (👊 = pi), Papier (✋ = pa) et Ciseaux (✌ = ci)')
score = 0
i = 0
continu = "t"
while i == 0 :
    if continu == "t" :
        if (random_choice =="pi" and user_choice == "ci") or (random_choice =="ci" and user_choice == "pa") or (random_choice =="pa" and user_choice == "pi") :
            print('Vous avez perdu')
        elif (user_choice =="pi" and random_choice == "ci") or (user_choice =="ci" and random_choice == "pa") or (user_choice =="pa" and random_choice == "pi")  : 
            print('Vous avez gagné')
            score = score + 1
        else :
            print("Match nul")
        print('Votre score est de : ',score)
        start = str(input('voulez vous continuer? t/f : '))
        if start != 't':
            break
        continu = start
        user_choice = input('Fais ton choix entre Pierre (👊 = pi), Papier (✋ = pa) et Ciseaux (✌ = ci) : ')
   

    