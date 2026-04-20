import sys
import time
import os

# ====================== FUNÇÃO DE ORDENAÇÃO (QuickSort) ======================
def partition(A, inicio, fim):
    """Função partition (Hoare) - exatamente como no slide (página 27)"""
    pivo = A[inicio]
    i = inicio - 1
    j = fim + 1
    
    while True:
        # Avança i até encontrar elemento >= pivo
        i = i + 1
        while A[i] < pivo:
            i = i + 1
        
        # Avança j até encontrar elemento <= pivo
        j = j - 1
        while A[j] > pivo:
            j = j - 1
        
        if i >= j:
            return j
        
        # Troca os elementos
        A[i], A[j] = A[j], A[i]


def quickSort(A, l, r):
    """Função principal recursiva - exatamente como no slide (página 28)"""
    if l < r:
        q = partition(A, l, r)
        quickSort(A, l, q)
        quickSort(A, q + 1, r)

def quick_sort(arr):
    """Função de interface (chama o quickSort com índices 0 e n-1)"""
    if len(arr) > 1:
        quickSort(arr, 0, len(arr) - 1)
    return arr


# ====================== FUNÇÕES AUXILIARES ======================
def ler_arquivo(nome):
    with open(nome, 'r') as f:
        linhas = f.readlines()
    dados = list(map(int, linhas[1:]))
    return dados


def testar_arquivo(arquivo):
    dados = ler_arquivo(arquivo)
    inicio = time.perf_counter()
    quick_sort(dados.copy())
    fim = time.perf_counter()
    tempo = fim - inicio
    return tempo


def salvar_resultados(resultados):
    nome_arquivo = "resultados_quick_sort.txt"
    with open(nome_arquivo, 'w') as f:
        f.write("Relatorio de Execucao - Quick Sort\n")
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
    
    print("\nIniciando testes: Quick Sort")
    print(f"Diretorio de instancias: {os.path.abspath(pasta_instancias)}\n")
    
    lista_resultados = testar_pasta(pasta_instancias)
    
    if lista_resultados:
        salvar_resultados(lista_resultados)
    
    print("\n" + "=" * 55)
    input("Execucao finalizada. Pressione ENTER para sair...")