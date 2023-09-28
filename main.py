# cree par Kevin Wen
# cree en 2023
# ce programme montre le code du TP2

# les commentaires du programme:
# ce programme montre un jeu de deviner les nombres

import random
# si le variable qui indique de continuer le jeu est yes on recommence le boucle while
continuer = 'yes'

while continuer == 'yes':

    randomNumber = random.randint(0, 100)
    nombreEssais= 1
    userNumber = int(input('donner un nombre entre 0 et 100:'))

    while userNumber != randomNumber:
        if userNumber < randomNumber:
            print('votre nombre est trop petit')
        elif userNumber > randomNumber:
            print('votre nombre est trop grand')
        nombreEssais += 1
        userNumber = int(input('donner un nombre entre 0 et 100:'))

    print('bravo! tu as eu la bonne reponse en faisant', str(nombreEssais),'essais')
    continuer = str(input('est-ce que vous voulez jouer encore? yes ou no?'))




print('merci et au revoir')