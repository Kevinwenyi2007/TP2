# cree par Kevin Wen
# cree en 2023
# ce programme montre le code du TP2

# les commentaires du programme:
# ce programme montre un jeu de deviner les nombres

import random

def game():# creer le fonction de game
    continuer = 'yes'# si le variable qui indique de continuer le jeu est yes on recommence le boucle while
    while continuer == 'yes':# lorsque l'utilisateur veut jouer, on commence le jeu

        randomNumber = random.randint(0, 100)
        nombreEssais= 1
        userNumber = int(input('donner un nombre entre 0 et 100:'))

        while userNumber != randomNumber:# quand la premiere reponse de l'utilisateur est fausse
            if userNumber < randomNumber:
                print('votre nombre est trop petit')
            elif userNumber > randomNumber:
                print('votre nombre est trop grand')
            nombreEssais += 1 # on ajoute 1 essai a chaque fois qu'un utilisateur a eu un mauvais reponse
            userNumber = int(input('donner un nombre entre 0 et 100:'))

        print('bravo! tu as eu la bonne reponse en faisant', str(nombreEssais),'essais')# indication que l'utilisateur a reussi
        continuer = str(input('est-ce que vous voulez jouer encore? yes ou no?'))# demander si l'utilisatuer veut jouer encore ou pas

game()
print('merci et au revoir')