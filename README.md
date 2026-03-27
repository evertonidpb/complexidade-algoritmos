# Comparativo de Algoritmos de Ordenação 

Este projeto implementa e analisa o desempenho de dois algoritmos clássicos de ordenação: **Insertion Sort** e **Selection Sort**, utilizando instâncias numéricas de diversos tamanhos.

## Sobre os Algoritmos

Ambos os algoritmos possuem complexidade de tempo de pior caso de O(n^2). 
- **Insertion Sort:** Eficiente para conjuntos de dados pequenos ou quase ordenados.
- **Selection Sort:** Mantém um número constante de trocas, mas realiza muitas comparações, sendo geralmente menos eficiente que o Insertion em dados aleatórios.

---

##  Como Executar os Testes

Cada script é independente e já contém a lógica de leitura de arquivos e medição de tempo.

### Pré-requisitos
* **Python 3.x** instalado.
* A pasta `instancias/` deve estar localizada no diretório pai do código (conforme a estrutura do projeto).

### Estrutura de Pastas
Para o funcionamento correto, mantenha a pasta de instâncias no diretório pai ou ajuste a variável `pasta_instancias` no código:
```text
/projeto
  ├── instancias/ (arquivos .in)
  └── src/
      ├── insertion_sort.py
      └── selection_sort.py

### Execução

Para testar o **Insertion Sort**, acesse a pasta src/ e execute:
```bash
python insertion_sort.py


Para testar o **Selection Sort**, acesse a pasta src/ e execute:
```bash
python selection_sort.py


### Funcionalidades do Script
Medição de Alta Precisão: Utiliza time.perf_counter() para capturar milissegundos com exatidão.

Relatórios Automáticos: Gera um arquivo .txt local (ex: resultados_insertion_sort.txt) contendo a tabela de tempos após a execução.

Interface Limpa: Exibe o progresso e os tempos formatados diretamente no terminal.

Prevenção de Fechamento: O script solicita uma tecla ao final da execução para que o usuário possa analisar os resultados no console sem que a janela feche sozinha.