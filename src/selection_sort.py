import sys
import time
import os

# --- FUNÇÃO DE ORDENAÇÃO ---
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        i_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[i_min]:
                i_min = j

        if arr[i] != arr[i_min]:
            temp = arr[i]
            arr[i] = arr[i_min]
            arr[i_min] = temp
    return arr

# --- FUNÇÕES AUXILIARES ---
def ler_arquivo(nome):
    with open(nome, 'r') as f:
        linhas = f.readlines()
    
    # Ignora a primeira linha (contém os valores de "n")
    if not linhas:
        return []
    dados = list(map(int, linhas[1:]))
    return dados

def testar_arquivo(arquivo):
    dados = ler_arquivo(arquivo)
    if not dados:
        return 0

    # Inicia a contagem de tempo de alta precisão
    inicio = time.perf_counter()
    selection_sort(dados.copy()) 
    fim = time.perf_counter()

    tempo = fim - inicio
    return tempo

def salvar_resultados(resultados):
    nome_arquivo = "resultados_selection_sort.txt"
    with open(nome_arquivo, 'w') as f:
        f.write("Relatorio de Execucao - Selection Sort\n")
        f.write("-" * 45 + "\n")
        f.write(f"{'Arquivo':<30} | {'Tempo (s)':<12}\n")
        f.write("-" * 45 + "\n")
        for arq, tempo in resultados:
            f.write(f"{arq:<30} | {tempo:.6f}\n")
    print(f"\n[OK] Resultados salvos com sucesso em: {nome_arquivo}")

def testar_pasta(pasta):
    if not os.path.exists(pasta):
        print(f"Erro: A pasta '{pasta}' nao foi encontrada.")
        return []

    resultados = []
    # Pega apenas arquivos, ignorando pastas, e ordena por nome
    arquivos = sorted([f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))])

    print(f"{'Arquivo':<30} | {'Tempo (s)':<12}")
    print("-" * 45)

    for arq in arquivos:
        caminho = os.path.join(pasta, arq)
        tempo = testar_arquivo(caminho)
        resultados.append((arq, tempo))
        print(f"{arq:<30} | {tempo:.6f}")

    return resultados

# --- BLOCO PRINCIPAL (MAIN) ---
if __name__ == "__main__":
    # Caminho relativo para a pasta com as instâncias
    pasta_instancias = "../instancias"

    print("\nIniciando testes: Selection Sort")
    print(f"Diretorio alvo: {os.path.abspath(pasta_instancias)}\n")

    # Executa a bateria de testes
    lista_resultados = testar_pasta(pasta_instancias)

    # Se a lista não estiver vazia, gera o arquivo .txt
    if lista_resultados:
        salvar_resultados(lista_resultados)

    print("\n" + "="*45)
    # Mantém o prompt aberto para visualização
    input("Execucao finalizada. Pressione ENTER para sair...")