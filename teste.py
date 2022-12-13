import functions
import tracemalloc

def main():
    
    functions.limparInicio()
    
    print("Para começar, digite o caminho para o arquivo do grafo: ")
    path = 'src/collaboration_graph.txt'
    
    G = functions.lerArquivoGrafos(path)
    
    functions.buscarComponentes(G)
    
main()

    