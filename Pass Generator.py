import os
from os import *

system("pip install random")
system("pip install string")
system("pip install art")
system("pip install termcolor")
system("cls")

import random
import string
from random import choice, randint
from art import *
from termcolor import colored

def main():
    
    #ascii art 
    print(colored(text2art ("\t______________\n"),'blue'))
    print(colored(text2art ("\t_PassGenerator_"),'white'))
    print(colored(text2art ("\t______________"),'red'))                      

    try:
        print("="*95)
        passwordl = input("Enter le Nb de Password : ")
        length = input("Entrer la longeur du Password : ")
        
        
        print("[+] Password en cours de Génération.....")
        
        print("Gérération de Password terminé !\n")

        #define data
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        letters = string.ascii_letters

        #combine the data
        all = lower + upper + num + symbols + letters
        
        #define k en nb password
        k = passwordl

        #use random 
        for password in range(1, int(passwordl) +1):
            print("".join(random.choices(all, k=int(length))))
        
        print("\tVoulez vous Refaire une Génération ? (y/n)")
        choice = input("\t> ")

        if choice == 'y':
            main()
        
        elif choice == 'n':
            print("\t[!] Au Revoir !!")


    except KeyboardInterrupt:
        print("\n\t[!] Vous avez appuyé sur ctrl + C pour quitter instantanément")

main()
