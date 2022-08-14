# Createur < Doc.Shaka >
# -*- coding: utf-8 -*-

# Instalation des Librairy

import os
from os import *

system("pip install random")
system("pip install string")
system("pip install art")
system("pip install termcolor")
system("cls")

# Librairy

import random
import string
from random import choice, randint
from art import *
from termcolor import colored

# Début de la DEF main

def main():
    
    #ascii art 

    print(colored(text2art ("\t______________\n"),'blue'))
    print(colored(text2art ("\t_PassGenerator_"),'white'))
    print(colored(text2art ("\t______________"),'red'))                      

    # Saisie des donnés

    try:
        print()

        passwordl = input("\n<PassGenerator>: Enter le Nb de Password : ")

        print()

        length = input("\n<PassGenerator>: Entrer la longeur du Password : ")

        print()

        print("\n<PassGenerator>: [+] Password en cours de Génération.....")

        # barre de chargement

        print("="*1)

        system("cls")

        print("="*10)

        system("cls")

        print("="*20)

        system("cls")

        print("="*30)

        system("cls")

        print("="*40)

        system("cls")

        print("="*50)

        system("cls")

        print("="*60)

        system("cls")

        print("="*70)

        system("cls")

        print("="*80)

        system("cls")

        print("="*90)

        system("cls")

        print("="*100)

        system("cls")

        # Code pure

        print()

        print("\n<PassGenerator>: Gérération de Password terminé !\n")

        # Définiton des data

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        letters = string.ascii_letters

        # Combine les data

        all = lower + upper + num + symbols + letters
        
        # Définition de k en nb password

        k = passwordl

        # Utilisation de Random

        for password in range(1, int(passwordl) +1):
            print()

            print("\n<PassGénèrator>: Voici le(s) mot(s) de passe généré ")

            print()

            print("".join(random.choices(all, k=int(length))))

        # Choix et loops du DEF main
        
        print()
        
        print("\n<PassGénèrator>: Voulez vous Refaire une Génération ? [y/n] ")

        print()

        choice = input("\n<PassGénèrator>: ")

        if choice == 'y':
            main()
        
        elif choice == 'n':
            
            print()
            
            print("\n<PassGénèrator>: [!] Au Revoir !!")

            print()

    except KeyboardInterrupt:

        print()

        print("\n\t[!] Vous avez appuyé sur ctrl + C pour quitter instantanément")

        print()

main() # Fin de la DEF main
