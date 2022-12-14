import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
from tqdm import tqdm
import matplotlib.pyplot as plt


def limparInicio():
    if os.path.isdir("resultados"):
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
    # np.set_printoptions(threshold=10000)
    try:
        if not os.path.isdir("resultados/visualizacao"):
            os.makedirs("resultados/visualizacao")

        A = nx.to_numpy_matrix(G)
        print("\n")
        with open('resultados/visualizacao/matriz.txt', 'w') as f:
            for i, line in tqdm(enumerate(A), total=len(A)):
                np.savetxt(f, line, fmt='%.0f')

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


# busca em largura
def buscaLargura(G, vertice):
    try:
        if not os.path.isdir("resultados/busca"):
            os.makedirs("resultados/busca")

        A = nx.path_graph(G)
        T = nx.dfs_tree(A, source=vertice).reverse().reverse()

        with open('resultados/busca/buscaLargura.txt', 'w') as f:
            f.write("vértice - pai - nível\n\n")
            lista = list(T.nodes)

            for i, node in tqdm(enumerate(T.nodes), total=len(lista)):
                listaAnc = list(nx.ancestors(T, node))
                pai = lista[i-1] if len(listaAnc) > 0 else 0
                nivel = len(listaAnc)
                f.write(f"{node} - {pai} - {nivel}\n")

        # nx.draw_networkx(T)
        # plt.show()

    except Exception as e:
        print(e)
        return False


def buscarComponentes(G):
    try:
        if not os.path.isdir("resultados/componentes"):
            os.makedirs("resultados/componentes")

        qnt = nx.number_connected_components(G)

        with open('resultados/componentes/componentes.txt', 'w') as f:
            f.write(f"Total de componentes: {qnt}\n")
            for i, comp in tqdm(enumerate(nx.connected_components(G)), total=qnt):
                lista = list(comp)
                f.write(f"\n\nCompontente [{i}] - {len(lista)} vértices\n")
                f.write(str(lista))

    except Exception as e:
        print(e)
        return False
