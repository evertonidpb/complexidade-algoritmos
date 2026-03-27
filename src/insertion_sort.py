import sys
import time
import os

# --- FUNÇÃO DE ORDENAÇÃO ---
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        pivo = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > pivo:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivo
    return arr

# --- FUNÇÕES AUXILIARES ---
def ler_arquivo(nome):
    with open(nome, 'r') as f:
        linhas = f.readlines()
    
    # Ignora a primeira linha (quantidade)
    dados = list(map(int, linhas[1:]))
    return dados

def testar_arquivo(arquivo):
    dados = ler_arquivo(arquivo)

    # Inicia a contagem de tempo
    inicio = time.perf_counter()
    insertion_sort(dados.copy()) 
    fim = time.perf_counter()

    tempo = fim - inicio
    return tempo

def salvar_resultados(resultados):
    nome_arquivo = "resultados_insertion_sort.txt"
    with open(nome_arquivo, 'w') as f:
        f.write("Relatorio de Execucao - Insertion Sort\n")
        f.write("-" * 40 + "\n")
        for arq, tempo in resultados:
            f.write(f"{arq}: {tempo:.6f} segundos\n")
    print(f"\n[OK] Resultados salvos com sucesso em: {nome_arquivo}")

def testar_pasta(pasta):
    if not os.path.exists(pasta):
        print(f"Erro: A pasta '{pasta}' nao foi encontrada.")
        return []

    resultados = []
    arquivos = sorted(os.listdir(pasta))

    print(f"{'Arquivo':<30} | {'Tempo (s)':<10}")
    print("-" * 45)

    for arq in arquivos:
        caminho = os.path.join(pasta, arq)
        
        # Verifica se é um arquivo
        if os.path.isfile(caminho):
            tempo = testar_arquivo(caminho)
            resultados.append((arq, tempo))
            print(f"{arq:<30} | {tempo:.6f}")

    return resultados

# --- BLOCO PRINCIPAL ---
if __name__ == "__main__":
    # Busca a pasta com as instâncias no caminho relativo dois níveis acima
    pasta_instancias = "../instancias"

    print("\nIniciando testes: Insertion Sort")
    print(f"Diretorio de instancias: {os.path.abspath(pasta_instancias)}\n")

    # Executa os testes
    lista_resultados = testar_pasta(pasta_instancias)

    # Se houve resultados, salva no arquivo
    if lista_resultados:
        salvar_resultados(lista_resultados)

    print("\n" + "="*45)
    # Impede o fechamento automático do prompt
    input("Execucao finalizada. Pressione ENTER para sair...")
