#!/usr/bin/env python
# coding: utf-8
from fonction.LFR import Fitch, Reconciliation
#Programme réalisé par Enody Gernet et Inès Liroulet

print()
print()
print("/!\ ATTENTION /!\ ")
print("1 - Veillez à bien installer le module Python 'newick' (!pip install newick) pour utiliser ce programme !")
print("2 - Vérifiez que vous lancez bien ce programme dans le même dossier que les fichiers d'exemple Entry.txt, Entry_gene.txt et Entry_espece.txt !")
print()
print()


def question():
    while True:
        try:
            cont = input("Voulez-vous continuer à utiliser le programme sur vos propres fichiers (y/n) ? : ")
            print()
        except ValueError:
            print("Veuillez répondre par 'y' ou 'n'.")
            print()
            continue
        else:
                break
    if cont=='y': 
        while True:
            try:
                alg = input("Quel algorithme voulez-vous utiliser ? Tapez 1 pour Fitch et 2 pour réconciliation : ")
                print()
            except ValueError:
                print("Veuillez répondre par 1 ou 2.")
                print()
                continue
            else:
                break
        if alg == "1":
            print("Veillez à bien mettre votre fichier dans le même dossier d'où vous lancez le programme.")
            print()
            file = str(input("Écrivez ici le nom du fichier contenant votre arbre (n'oubliez pas l'extension !) : "))
            print()
            Fitch(file)
            question()
        if alg == "2":
            print("Veillez à bien mettre vos fichiers dans le même dossier d'où vous lancez le programme.")
            print()
            file_gene = str(input("Écrivez ici le nom du fichier contenant votre arbre de gènes (n'oubliez pas l'extension !) : "))
            print()
            file_espece = str(input("Écrivez ici le nom du fichier contenant votre arbre d'espèces (n'oubliez pas l'extension !) : "))
            print()
            Reconciliation(file_gene, file_espece)
            question()
    if cont=='n':
        exit

#Démonstration des algorithmes

if __name__ == '__main__':

    print()
    print("Exemples d'utilisation des algorithmes avec les fichiers exemples inclus :")
    print()

    #Exemple de Fitch et LCA

    Fitch("Entry.txt", exempleLCA=True)
    
    #Exemple de réconciliation

    Reconciliation("Entry_gene.txt", 'Entry_espece.txt')

    print()
    print()
    print()

    question()

    
    
        