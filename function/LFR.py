#Module utilisé pour l'affichage graphique des arbres (en ASCII)
import newick
from newick import loads
from newick import read
from .tree_search import listspecies, Postorder, Preorder
from .tree_process import read_file, newick_to_tree, nodes_to_newick
from .tree_modify import PostorderGene, PreorderGene, LCA


#Fonction de parcimonie qui permet de reconstruire l’évolution des caractères sur un arbre.
def Fitch(fichier, exempleLCA=False):
    print()
    print("Algorithme de Fitch :")
    print()
    #Lecture du fichier
    print("Lecture du fichier...")
    newick = read_file(str(fichier))
    #Création d'un arbre à partir d'un Newick
    root = newick_to_tree(newick) 
    # Utilisation des fonctions pour Fitch
    print()
    print("Traversée postorder :")
    Postorder(root)    
    Postorder_ascii = nodes_to_newick(root)+";" #Stockage de l'arbre après Postorder
    print()
    print(loads(Postorder_ascii)[0].ascii_art()) #Affichage de l'arbre
    print()
    print("Traversée preorder :")
    Preorder(root)
    Preorder_ascii = nodes_to_newick(root)+";" #Stockage de l'arbre après Preorder
    print()
    print(loads(Preorder_ascii)[0].ascii_art()) #Affichage de l'arbre
    print()
    if exempleLCA==True:
        print()
        print("LCA (Last Common Ancestor):")
        print()
        print("Exemple d'utilisation de l'algorithme LCA pour trouver l'ancêtre commun de deux noeuds :")
        print("- les deux noeuds pris en exemple sont le noeud",root.left.left.left.name,"et",root.left.right.right.name,"(du même côté de l'arbre à partir de la racine)")
        print()
        print("- résultat de notre algorithme :")
        LCA(root.left.left.left,root.left.right.right)
        print()
        print("- vérification manuelle : l'adresse du bon LCA est :",root.left)
        print()
        print()

#Fonction qui permet de faire l'alignement d’un arbre de gènes sur un arbre d’espèces pour détecter des duplications et des pertes.
def Reconciliation(fichier_gene, fichier_espece):
    print()
    print("Algorithme de réconciliation :")
    print()
    #Lecture des fichiers
    print("Lecture des fichiers...")
    newick_gene = read_file(str(fichier_gene))
    newick_espece = read_file(str(fichier_espece))
    #Stockages des arbres de gènes et d'espèces
    root_gene = newick_to_tree(newick_gene) 
    root_espece = newick_to_tree(newick_espece) 
    #Affichage des espèces
    list_species = []
    list_species = listspecies(root_espece,list_species)
    print("Liste des espèces comprises dans l'arbre d'espèces :")
    print(list_species)
    print()
    print()
    print("Traversée postorder :")
    PostorderGene(root_gene, list_species, root_espece) 
    PostorderGene_ascii = nodes_to_newick(root_gene)+";"
    print()
    print(loads(PostorderGene_ascii)[0].ascii_art())
    print()
    print("Traversée preorder :")
    PreorderGene(root_gene, root_espece)
    PreorderGene_ascii = nodes_to_newick(root_gene)+";"
    print()
    print(loads(PreorderGene_ascii)[0].ascii_art())
    print()
