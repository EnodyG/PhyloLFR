from .tree_search import intersection, findspecies, remplacement, LCA
from .tree_process import Node
    

#Fonction qui va permettre de faire correspondre l'arbre de gènes à l'arbre d'espèces 
#tout en remontant l'information des gènes
def PostorderGene(node,liste,root_espece):
    if node == None:
        return

    # récursivité sur fils gauche
    PostorderGene(node.left,liste,root_espece)
    # récursivité sur fils droit
    PostorderGene(node.right,liste,root_espece)

    # On traite le noeud
    if node.left == None and node.right == None:
        if intersection(node.name[0],liste) != []:
            node.name = intersection(node.name[0],liste)
        else: 
            return("Arbres d'espèces et de gènes non conformes")
    else:
        geneA = findspecies(node.left,root_espece)
        geneB = findspecies(node.right,root_espece)
        
        node.name = LCA(geneA,geneB).name
        
    print("( ",node.name,")")


#Fonction qui va apporter les évènements de spéciation et de duplication sur l'arbre de gènes
#Méthode qui va apporter les évènements de spéciation et de duplication sur l'arbre de gène
def PreorderGene(node,root_espece):
    if node == None:
        return
    
    #On vérifie que les noeuds sont des noeuds internes
    if node.left != None or node.right != None:
        gene = findspecies(node,root_espece)
        if gene.left != None or gene.right != None:
            #On attribut un evenement
            if node.name == node.left.name and node.name == node.right.name:
                node.label = "Duplication"
            else:
                node.label = "Speciation"
                #Dans le cas de la spéciation on vérifie si le gene se trouve à gauche ou à droite et ensuite on transmet
                #l'info depuis l'arbre d'espece vers l'arbre de gene (avec l'eventuelle perte)
                
                if node.left.name != gene.left.name and node.left.name != gene.right.name and node.left.name != node.name:
                    if findspecies(node.left,gene.left) != None:
                        remplacement(node.left,Node(gene.left.name))
                    elif findspecies(node.left,gene.right) != None:
                        remplacement(node.left,Node(gene.right.name))

                        
                if node.right.name != gene.left.name and node.right.name != gene.right.name and node.right.name != node.name:
                    if findspecies(node.right,gene.left) != None:
                        remplacement(node.right,Node(gene.left.name))
                        
                    elif findspecies(node.right,gene.right) != None:
                        remplacement(node.right,Node(gene.right.name))
    #récursivité fils gauche
    PreorderGene(node.left,root_espece)
    #récursivité fils droit
    PreorderGene(node.right,root_espece)

