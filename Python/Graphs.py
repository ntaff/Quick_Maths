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