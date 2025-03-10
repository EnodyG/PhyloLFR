

# Fonction de lecture de fichier
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            newick = file.read()
            if newick.endswith('\n'):
                newick[:-1]  # Enlever le dernier saut de ligne s'il y en a un
            newick_tree = list(newick)
            return newick_tree
        
    except FileNotFoundError:
        print(f"Fichier non trouvé : {file_path}")
        print("Vérifiez que vous lancez bien cet algorithme dans le même dossier que les fichiers à utiliser.")
        print()
    
    except Exception as e:
        print(f"Le fichier n'a pas pu être lu à cause de l'erreur suivante : {e}")
        print()


# Définition de la structure noeud utilisée pour implémenter l'arbre (structure consensus trouvable en ligne et modifiée)
class Node:
    def __init__(self, name, label=None, left=None, right=None, parent=None):
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.label = label
    
    #Méthode pour ajouter un noeud parent
    def add_child(self, child, direction=None):
        if direction == "left":
            child.parent = self
            self.left = child
        elif direction == "right":
            child.parent = self
            self.right = child
        else:
            print("Erreur, l'ajout d'un fils doit se faire à droite ou à gauche !")
        return None
    
    #Méthode pour ajouter un noeud enfant
    def add_parent(self, parent, direction):
        parent.add_child(self, direction)
        return None
    
    #Méthode pour vérifier si un noeud est une feuille
    def is_leaf(self):
        if self.left == None and self.right == None:
            leaf = True
        else :
            leaf = False
        return leaf


# Fonction pour obtenir une structure de noeuds à partir d'un arbre en format Newick
def newick_to_tree(newick_tree):
    root = Node([],"root")
    def construct_recursive(newick_tree,current_node):
        if newick_tree[0] == "(":
            current_node.add_child(Node([]),"left")
            construct_recursive(newick_tree[1:],current_node.left)
        elif newick_tree[0]== ",":
            current_node.parent.add_child(Node([]),"right")
            construct_recursive(newick_tree[1:],current_node.parent.right)
        elif newick_tree[0] == ")":
            construct_recursive(newick_tree[1:],current_node.parent)
        elif newick_tree[0].isalpha() == True:
            current_node.name = [newick_tree[0]]
            construct_recursive(newick_tree[1:],current_node)
        elif newick_tree[0].isnumeric() == True:
            construct_recursive(newick_tree[1:],current_node)
            
    construct_recursive(newick_tree,root)               
    return root


# Fonction pour générer un arbre en format Newick à partir d'une structure de noeuds
# Inspirée de la fonction de Daphné Navratil
def nodes_to_newick(node):
    
    if not node.is_leaf(): #Si le noeud n'est pas une feuille
    
        left_node = nodes_to_newick(node.left) #récursivité sur enfant gauche
        right_node = nodes_to_newick(node.right) #récursivité sur enfant droit
        
        #La fonction retourne entre parenthèses le nom des noeuds enfants séparés par une virgule, 
        # et après la parenthèse le nom du noeud
        newick_tree = f"({left_node},{right_node}){''.join(node.name)}" 
    else:
        #Si le noeud est une feuille, la fonction retourne le nom du noeud
        newick_tree = ''.join(node.name) 
                     
    return newick_tree


