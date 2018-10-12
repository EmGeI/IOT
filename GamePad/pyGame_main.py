#!/usr/bin/python3
####################################################
##
## File : pyGame_main.py
## Created : 2018-10-12
## Author : Greg MUNTEN
##
####################################################
""" Ce programme affiche les différentes entrée d'une manette de jeux.
Pour fonctionner, il faudra au préalable installer pyGame via la commande
sudo pip install pygame pour python2.x
sudo pip3 install pygame pour python 3.x

Testé :
Buffalo Classic USB Gamepad ( Famicom NES Type) : les boutons \"Clear\" et \"Turbo\" ne sont pas reconnues"""

import pygame as p # Import de la bibiothèque pygame
p.init() # Initialisation de la bibliothèque
nb_stick = p.joystick.get_count()# calculer le nombre de manette connecter

if nb_stick > 0: # si il y a au moins une manette 
    stick = p.joystick.Joystick(0) # je prends le 1ere manette que je trouve
    stick.init() # je l'initialise

    print("Axes :", stick.get_numaxes()) # On imprime le nombre d'axes
    print("Boutons :", stick.get_numbuttons()) # On imprime le nombre de boutons
    
    nb_boutons = stick.get_numbuttons() # on récupère le nombre de boutons dans une variable
    if nb_boutons >= 4: # on vérifie qu'il y en a a au moins 4
        continuer = 1

        while continuer:
            for event in p.event.get():
                print(event)
    else:
        print("Votre joystick ne possède pas au moins 4 boutons")
else:
    print("Vous n'avez pas branché de manette...")
