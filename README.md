# Comparativo de Algoritmos de Ordenação 

Este projeto implementa e analisa o desempenho de **quatro algoritmos clássicos de ordenação**: **Insertion Sort**, **Selection Sort**, **Merge Sort** e **Quick Sort**, utilizando instâncias numéricas de diversos tamanhos.

## Sobre os Algoritmos

- **Insertion Sort** e **Selection Sort**  
  Complexidade de tempo de **pior caso O(n²)**.  
  Eficientes para conjuntos de dados pequenos ou quase ordenados.

- **Merge Sort**  
  Baseado no paradigma **Divisão e Conquista** (exatamente como apresentado na Aula 6).  
  Complexidade **O(n log n)** em todos os casos (melhor, médio e pior).  
  Usa a função `merge` com sentinelas para combinar as soluções dos subproblemas.

- **Quick Sort**  
  Baseado no paradigma **Divisão e Conquista** (versão Hoare apresentada na Aula 6).  
  Complexidade **O(n log n)** no caso médio e melhor, **O(n²)** no pior caso.  
  Usa a função `partition` com pivô no primeiro elemento.

---

## Como Executar os Testes

Cada script é **independente** e já contém toda a lógica de leitura de arquivos, medição de tempo com `time.perf_counter()`, geração de relatório e prevenção de fechamento do terminal.

### Pré-requisitos
- **Python 3.x** instalado.
- A pasta `instancias/` deve estar localizada no diretório **pai** do código (conforme a estrutura do projeto).

### Estrutura de Pastas
Para o funcionamento correto, mantenha a seguinte estrutura:

```text
/projeto
  ├── instancias/          (arquivos .in com as instâncias de teste)
  └── src/
      ├── insertion_sort.py
      ├── selection_sort.py
      ├── merge_sort.py
      └── quick_sort.py
    
```

### Execução

Para testar o **Insertion Sort**, acesse a pasta src/ e execute:

```bash
python insertion_sort  
``` 
ou

```bash
python .\insertion_sort  
``` 

Para testar o **Selection Sort**, acesse a pasta src/ e execute:

```bash
python selection_sort.py
```

ou

```bash
python .\selection_sort.py
```

Para testar o **Merge Sort**, acesse a pasta src/ e execute:

```bash
python merge_sort.py
```

ou

```bash
python .\merge_sort.py
```


Para testar o ** Quick Sort**, acesse a pasta src/ e execute:

```bash
python quick_sort.py
```

ou

```bash
python .\quick_sort.py
```


### Funcionalidades do Script

1 - Medição de alta precisão com time.perf_counter().

2 - Relatório automático gerado em arquivo .txt:
  A - resultados_insertion_sort.txt
  B - resultados_selection_sort.txt
  C - resultados_merge_sort.txt
  D - resultados_quick_sort.txt

3 - Interface limpa no terminal com tabela de tempos.

4 - Ao final da execução, o script aguarda você pressionar ENTER para não fechar a janela automaticamente.