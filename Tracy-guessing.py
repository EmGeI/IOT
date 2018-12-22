#!/usr/bin/python3

import random

def verify():
    secret=random.randint(1,10)
    for guesstaken in range(1,7):
	    print("\nChoisi un nombre! ")
	    guess=int(input())
	    if(guess<secret):
		    print("Votre nombre est trop bas!")
	    elif(guess>secret):
		    print("Votre nombre est trop haut!")
	    else:
		    break

    if(guess==secret):
	    print("*********** Vous avez gagné ***********")
	    print("Votre nombre est correct " + str(guess))
	    print("Vous avec trouvé en "+str(guesstaken) +" essais")
    else:
	    print("*********** Vous avez perdu **********")
	    print("Vous avez utilisé "+str(guesstaken) +" essais")
	    print("Le nombre à trouver était "+ str(secret))

verify()
