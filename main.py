import functions;
import tracemalloc;

print("\n\n ------ Bem vindo ao nosso trabalho 1! ------ \n\n")

def main():
    
    functions.limparInicio()
    
    print("Para começar, digite o caminho para o arquivo do grafo: ")
    path = str(input())

    while(functions.validarArquivo(path) == False):
        print("\n ❌ OPS! Esse arquivo não existe. ❌\n\nPor favor, tente novamente:")
        path = str(input())
    
    G = functions.lerArquivoGrafos(path)
    
    if(functions.gerarArquivoSaida(G) == True):
        print("\n✅ Arquivo de saída salvo com sucesso! ✅\n")
    else:
        print("❌ Erro ao salvar o arquivo de saída! ❌")
        exit()
 

        
    #Opções de visualização
    print("\nEscolha a forma de visualização que seja utilizar:")
    print("[ 1 ] Matriz de adjacências\n[ 2 ] Lista de adjacências\n[ 3 ] Lista e Matriz de adjacências\n")
    visualizacao = (input("Opção: "))

    while(visualizacao != '1' and visualizacao != '2' and visualizacao != '3'):
        print("\n ❌ OPS! Essa opção não existe. ❌\n\nPor favor, tente novamente:")
        visualizacao = (input("Opção: "))
    
    tracemalloc.start()
    
    if(visualizacao == '1'):
        matriz = functions.criarMatriz(G)
        print("\n✅ Matriz de adjacências salva com sucesso! ✅\n") if matriz == True else print("\n❌ Erro ao salvar a Matriz de adjacências! ❌\n")
    
    elif(visualizacao == '2'):
        lista = functions.criarLista(G)
        print("\n✅ Lista de adjacências salva com sucesso! ✅\n") if lista == True else print("\n❌ Erro ao salvar a lista de adjacências! ❌\n")
        
    elif(visualizacao == '3'):
        matriz = functions.criarMatriz(G)
        print("\n✅ Matriz de adjacências salva com sucesso! ✅\n") if matriz == True else print("\n❌ Erro ao salvar a Matriz de adjacências! ❌\n")
        
        lista = functions.criarLista(G)
        print("✅ Lista de adjacências salva com sucesso! ✅\n") if lista == True else print("\n❌ Erro ao salvar a lista de adjacências! ❌\n")
    
    second_size, consumoMem = tracemalloc.get_traced_memory()
    print('Consumo de memória: ', f'{"{:.3f}".format(consumoMem / 10**6)}MB')
    # stopping the library
    tracemalloc.stop()
    
main()

    