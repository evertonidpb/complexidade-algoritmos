import sys
import time
import os

# ====================== FUNÇÃO DE ORDENAÇÃO (MergeSort) ======================
def merge(A, p, q, r):
    """Função merge - exatamente como no slide (página 17)"""
    # Cria L e R com sentinela INF (índices iniciam em 1, conforme slide)
    L = [None] + A[p:q+1] + [float('inf')]
    R = [None] + A[q+1:r+1] + [float('inf')]
    
    i = 1
    j = 1
    for k in range(p, r + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSort(A, p, r):
    """Função principal recursiva - exatamente como no slide (página 15)"""
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

def merge_sort(arr):
    """Função de interface (chama o mergeSort com índices 0 e n-1)"""
    if len(arr) > 1:
        mergeSort(arr, 0, len(arr) - 1)
    return arr


# ====================== FUNÇÕES AUXILIARES ======================
def ler_arquivo(nome):
    with open(nome, 'r') as f:
        linhas = f.readlines()
    # Ignora a primeira linha (quantidade de elementos)
    dados = list(map(int, linhas[1:]))
    return dados


def testar_arquivo(arquivo):
    dados = ler_arquivo(arquivo)
    inicio = time.perf_counter()
    merge_sort(dados.copy())          
    fim = time.perf_counter()
    tempo = fim - inicio
    return tempo


def salvar_resultados(resultados):
    nome_arquivo = "resultados_merge_sort.txt"
    with open(nome_arquivo, 'w') as f:
        f.write("Relatorio de Execucao - Merge Sort\n")
        f.write("-" * 50 + "\n")
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
        if os.path.isfile(caminho):
            tempo = testar_arquivo(caminho)
            resultados.append((arq, tempo))
            print(f"{arq:<30} | {tempo:.6f}")
    
    return resultados


# ====================== BLOCO PRINCIPAL ======================
if __name__ == "__main__":
    pasta_instancias = "../instancias"
    
    print("\nIniciando testes: Merge Sort")
    print(f"Diretorio de instancias: {os.path.abspath(pasta_instancias)}\n")
    
    lista_resultados = testar_pasta(pasta_instancias)
    
    if lista_resultados:
        salvar_resultados(lista_resultados)
    
    print("\n" + "=" * 55)
    input("Execucao finalizada. Pressione ENTER para sair...")