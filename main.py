# cree par Kevin Wen
# cree en 2023
# ce programme montre le code du TP2

# les commentaires du programme:
# ce programme montre un jeu de deviner les nombres

import random

# creer le fonction de jeu de number guesser
def game():
    # si le variable qui indique de continuer le jeu est yes on recommence le boucle while
    continuer = 'yes'

    # lorsque l'utilisateur veut jouer, on commence le jeu
    while continuer == 'yes':

        min = int(input('choisi le nombre minimum de interval du jeu'))
        max = int(input('choisi le nombre maximum de interval du jeu'))

        randomNumber = random.randint(min, max)
        nombreEssais= 1
        userNumber = int(input('donner un nombre aleatoire de votre interval:'))

        # quand la premiere reponse de l'utilisateur est fausse et on le donne des indices pour arriver a la bonne reponse
        while userNumber != randomNumber:
            if userNumber < randomNumber:
                print('votre nombre est trop petit')
            elif userNumber > randomNumber:
                print('votre nombre est trop grand')

            nombreEssais += 1
            userNumber = int(input('donner un nombre entre 0 et 100:'))


        print('bravo! tu as eu la bonne reponse en faisant', str(nombreEssais),'essais')
        continuer = str(input('est-ce que vous voulez jouer encore? yes ou no?'))

game()
print('merci et au revoir')