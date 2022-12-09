import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

def limparInicio():
    shutil.rmtree('resultados')

def validarArquivo(path):
    return os.path.isfile(path)


def lerArquivoGrafos(path):

    # carregar os nós
    with open(path) as f:
        pares = f.read().splitlines()

    # pega os nós em duas listas separadas
    node_1 = []
    node_2 = []

    # separando os nós em listas separadas
    for i, cont in zip(pares, range(len(pares))):

        if cont == 0:
            qnt = i
            continue  # ignora a primeira linha

        node_1.append(i.split(' ')[0])
        node_2.append(i.split(' ')[1])

    # cria um dataframe PANDAS para armazenar os dados
    df = pd.DataFrame({'node_1': node_1, 'node_2': node_2})

    G = nx.from_pandas_edgelist(
        df,
        "node_1",
        "node_2",
        create_using=nx.Graph()
    )
    
    return G


def gerarArquivoSaida(G):
    try:
        if not os.path.isdir("resultados"):
            os.makedirs("resultados")
            
        with open('resultados/saida.txt', 'w') as f:
            f.write("# n = {0}\n".format(G.number_of_nodes()))
            f.write("# m = {0}\n".format(G.number_of_edges()))
            for i, count in G.degree():
                f.write("{0} {1}\n".format(i, count))
        
        return True
    
    except Exception as e:
        print(e)
        return False
   


# Criar matriz de adjacência
def criarMatriz(G):
    try:
        if not os.path.isdir("resultados/visualizacao"):
            os.makedirs("resultados/visualizacao")
            
        A = nx.to_scipy_sparse_array(G)
        dense = A.todense()
        np.savetxt("resultados/visualizacao/matriz.txt", dense, fmt='%s', delimiter=",")
        
        return True

    except Exception as e:
        print(e)
        return False

# Criar lista de adjacência
def criarLista(G):
    try:
        if not os.path.isdir("resultados/visualizacao"):
            os.makedirs("resultados/visualizacao")
            
        nx.write_adjlist(G, "resultados/visualizacao/lista.txt")
    
        return True

    except Exception as e:
        print(e)
        return False