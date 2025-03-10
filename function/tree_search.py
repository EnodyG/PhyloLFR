import random
from .tree_process import Node

#Méthodes pour le LCA
#Fonction qui permets de retourner l'ancêtre commun le plus récent en se servant 
#de l'intersection des listes des parents des deux noeuds concernés
def LCA(node1,node2,print_msg=True):
    if node1 == None or node2 == None:
        return
    else:
        liste_parent_node1 =  []
        liste_parent_node2 =  []
        liste_parent_node1.append(node1)
        liste_parent_node2.append(node2)
        getparent(node1,liste_parent_node1)
        getparent(node2,liste_parent_node2)
        lca = intersection(liste_parent_node1,liste_parent_node2)[0]
        if print_msg==True:
            print("Le LCA de ces deux noeuds est :", lca.name, "( adresse du noeud :",lca,")")
        
        return lca
    
#Fonction qui renvoie sous forme de liste, l'intersection de deux listes
def intersection(listeA, listeB):
    sortie = [value for value in listeA if value in listeB]
    return sortie

  
#Fonction qui, de manière récursive, va récupérer tout les parents d'un noeud
def getparent(node, liste):
    if node == None:
        return
    if node.parent != None:
        liste.append(node.parent)
        getparent(node.parent,liste)


#Méthode pour la traversée d'arbre (appliquée pour Fitch)

# Fonction pour parcourir l'arbre en mode "post-order", type de parcours en profondeur 
#qui étudiera les fils avant d'étudier un potentiel parent
def Postorder(node):
    if node == None:
        return
    # D'abord récursivité sur fils gauche
    Postorder(node.left)
    # Puis récursivité sur fils droit
    Postorder(node.right)
    # Ensuite on traite le noeud
    print("(",node.name,")")
    if node.label != "root":
        print(node.parent)
        if intersection(node.name, node.parent.name) != []:
            node.parent.name = intersection(node.name, node.parent.name)
        else:
            node.parent.name = node.parent.name + node.name

# Fonction pour parcourir l'arbre en mode "pre-order", type de parcours en profondeur 
# qui étudiera un noeud parent puis ses fils            
def Preorder(node):
    if node == None:
        return
    if node.parent == None:
        node.name = [random.choice(node.name)]
    elif node.left != None or node.right != None:
        if intersection(node.name, node.parent.name) == []:
            node.name = [random.choice(node.name)]
        else:
            node.name = intersection(node.name, node.parent.name)
    # On traite le noeud
    print("(",node.name,")")
    # Puis récursivité sur fils gauche
    Preorder(node.left)
    # Et récursivité sur fils droit
    Preorder(node.right)



#Méthode pour la réconciliation

#Fonction qui va créer une liste des espèces existantes.
def listspecies(node,liste):
    if node == None:
        return liste
    # On traite le noeud
    liste.append(node.name[0])
    # récursivité sur fils gauche
    listspecies(node.left,liste)
    # récursivité sur fils droit
    listspecies(node.right,liste)
    return liste
    
#Fonction qui va vérifier dans l'arbre d'espèce une correspondance avec l'arbre de gène
def findspecies(node,root):
    if root != None:  
        # On traite le noeud
        if node.name == root.name:
            return root
  
        # récursivité sur fils gauche
        left = findspecies(node,root.left)
        if left is not None:
            return left
        # récursivité sur fils droit
        right = findspecies(node,root.right)
        if right is not None:
            return right
    return None 


#Méthodes pour la phase descendante de l'algorithme de réconciliation
def remplacement(node,remplacant):
    if node == None:
        return 
    
    if node.parent.left == node:
        remplacant.add_parent(node.parent,"left")
        node.parent.add_child(remplacant,"left")
        remplacant.add_child(node,"left")
        remplacant.add_child(Node("perte"),"right")
        node.add_parent(remplacant,"left")
    else:
        remplacant.add_parent(node.parent,"right")
        node.parent.add_child(remplacant,"right")
        remplacant.add_child(node,"right")
        remplacant.add_child(Node("perte"),"left")
        node.add_parent(remplacant,"right")

