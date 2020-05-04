import lib.graphslib as Vector
from copy import deepcopy

#########################
#### Oriented graphs ####
#########################

def nbSommets(G):
    return len(G)-1

def nbArcs(G):
    return len(G)
    
def ajoutArc(G,i,j):
    G[i].append(j)
    
def enleveArc(G,i,j):
    G[i].remove(j)
           
def degS(G,i):
    return len(G[i])

def degreS(G):
    D=[]
    for i in range(1,len(G)):
        D.append(degS(G,i))
    return D

def degE(G,i):
    x = 0
    for k in range(len(G)):
        for j in G[k]:
            if j==i :
                x+=1
    return x
           
def voisinage(G,i):
    L =[]
    for k in range(len(G)):
        for j in range(len(G[k])):
             if G[k][j]==i :
                L.append(k)
    return L

def degreE(G):
    D=[]
    for i in range(1,len(G)):
        D.append(degE(G,i))
    return D     

def listeToMatrice(G):
    M = Vector.initMat(len(G) - 1, 0)
    for i in range(1, len(G)):
        for j in G[i]:
            M[i - 1][j - 1] += 1
    return M


def areteToListe(n, L):
    G = Vector.initVectList(n + 1)
    for i in range(len(L)):
        G[L[i][0]].append(L[i][1])

    return G


def matToListe(M):
    G = Vector.initVectList(len(M) + 1)
    for i in range(len(M)):
        for j in range(len(M[i])):
            x = M[i][j]
            while x > 0:
                G[i + 1].append(j + 1)
                x = x - 1
    return G

#############################
#### Non-Oriented graphs ####
#############################

def nbSommets(G):
    return (len(G)-1)

def nbArete(G):
    n = 0
    for sommet in G:
        n += len(sommet)
    return n

def ajouteArete(G,  i, j):
     G.append([i, j])
     return G

def enleveArete(G, i, j):
    G[i].remove(j)
    G[j].remove(i)
    return G

def deg(G, i):
    return len(G[i])

def degre(G):
    V = Vector.initVect((len(G)-1), 0)
    print(V)
    for sommet in range(1, len(G)):
        V[sommet-1]=deg(G, sommet)
    return V

def listeToMatrice(G):
    matAdj = Vector.initMat((len(G) - 1), 0)
    for i in range(1,len(matAdj)):
        for j in range(1, len(matAdj[i])):
            for k in G[i+1]:
                 if k == j+1:
                     matAdj[i][j] = matAdj[i][j]+1
    return matAdj

def nonOriente(G):
        matAdj=listeToMatrice(G)
        for i in range(len(matAdj)-1):
            for j in range(len(matAdj)-1):
                if matAdj[i][j] != matAdj[j][i]:
                    return False
        return True

def kuratowski(n):
    V = Vector.initVectList(n+1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                pass
            else:
                V[i].append(j)
    return V

def areteToListe(n, L):
    V = Vector.initVectList(n)
    for i in range(0,len(L)):
            V[L[i][0]].append(L[i][-1])
            V[L[i][-1]].append(L[i][0])
    return V

def matriceToListe(M):
    V = Vector.initVectList(len(M) + 1)
    for i in range(len(M)):
        for j in range(len(M[i])):
            x = M[i][j]
            while x > 0:
                V[i + 1].append(j + 1)
                x = x - 1
    return V

def sousG(G,i):
    H = deepcopy(G)
    while H[i]!=[]:
        H[i].pop()
    return H

##############################
#### Breadth First Search ####
##############################

# Breadth First Search implementation starting at a specicied node (i)
def largeur(G, i):
    Visite = Vector.initVect(len(G), False) 
    File = [i] 
    ordreVisite = [] 
    Visite[i] = True  
    while len(File) != 0: 
        x = File[0] 
        File.pop(0)
        ordreVisite.append(x) 
        for succ in G[x]:
            if Visite[succ] == False: 
                Visite[succ] = True
                File.append(succ)
    return ordreVisite

# Generalized Breadth First Search implementation
def largeurG(G):
    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []
    File = []
    for i in range(1, len(G)):
        if Visite[i] == 0:
            ordreSousVisite = []
            File.append(i)
            Visite[i] = 1
            while File:
                y = File.pop(0)
                ordreSousVisite.append(y)
                for z in G[y]:
                    if Visite[z] == 0:
                        Visite[z] = 1
                        File.append(z)
                        else:
                        pass
            ordreVisite.append(ordreSousVisite)
    return ordreVisite

############################
#### Depth First Search ####
############################

# Depth First Search recursive auxiliary function starting from a specified node (i)
def profRec(G, i, Visite, ordreVisite):
    Visite[i] = 1
    ordreVisite.append(i)  
    for y in G[i]:
        if Visite[y] == 0:
            profRec(G, y, Visite, ordreVisite)
        else:
            pass

# Depth First Search implementation starting at a specicied node (i)
def profond(G, i):
    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []
    profRec(G, i, Visite, ordreVisite)
    return ordreVisite

# Generalized Depth First Search implementation
def profondG(G):
    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []
    for i in range(1, len(G)):
        if Visite[i] == 0:
            ordreSousVisite = []
            profRec(G, i, Visite, ordreVisiteRec)
            ordreVisite.append(ordreVisiteRec)
    return ordreVisite


####################################################
#### Search applications on Non-Oriented graphs ####
####################################################

 # G is connexe only if generalized DFS return only one connexe component
def isConnexe(G):
    return len(profondG(G)) == 1

# is_cyclic() func
def cyclicRec(G, pere, visite, cycle):
    if cycle[0]: 
        return 
    visite[pere] = True  
    for voisin in G[pere]:
        if visite[voisin] and voisin != pere: 
            cycle[0] = True 
            return
        if not visite[voisin]:
            cyclicRec(G, voisin, visite, cycle) 
        else:
            pass
    
# Return true if G is cyclic
def is_cyclic(G):
    visite = Vector.initVect(len(G), False) 
    cyclic = [False]
    for y in range(0, len(G)):
        if not visite[y]: 
            cyclicRec(G, y, visite, cyclic)
        if cyclic[0]: 
            break 
    return cyclic[0]

#G is a tree if he's connexe but not cyclic.
def isArbre(G):
    return isConnexe(G) and not is_cyclic(G) 

#Return the shortest paths between i and the other nodes
def plusCourtChemin(G, i):
    Visite = initVect(len(G), 0) 
    Pere = initVect(len(G), 0) 
    Distance = initVect(len(G),-1)
    Distance[i] = 0
    Pere[i] = i 
    File = [i] 
    Visite[i]=1 
    while len(File) != 0:
        y = File.pop(0) 
        for z in G[y]: 
            if Visite[z] == 0: 
                Visite[z] = 1
                File.append(z) 
                Distance[z] = Distance[y]+1 
                Pere[z]=y 
            else:
                pass
    return Distance, Pere

# Return if g is bipartite graph
def is_biparti(G):
    X=[]
    Y=[]
    Visite=Vector.initVect(len(G),0)
    File=[]
    for i in range(1,len(G)):
        if Visite[i]==0:
            Visite[i]=1
            File.append(i)
            X.append(i)
            while len(File)!=0:
                 y=File.pop()
                 for z in G[y]:
                     if Visite[z]==0:
                         File.append(z)
                         if Visite[y]==1:
                             Visite[z]=2
                             Y.append(z)
                         else:
                             Visite[z]=1
                             X.append(z)
                     else:
                        if Visite[z]==Visite[y]:
                            return False
    return True,X,Y

#Return the number of nodes in i's connexe component, with 
def TCC(G,i):
    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []
    prof = Vector.initVect(len(G), 0)
    profRec(G, i, Visite, ordreVisite, prof)
    return len(ordreVisite)
