# 📚 Bibliotecas Úteis em Bioinformática (Python)

Na bioinformática, Python é uma das linguagens mais usadas, e algumas bibliotecas se destacam por facilitar análises de dados biológicos. Aqui estão as principais:

---

## **1. BioPython**

* **Função**: Biblioteca especializada em bioinformática.
* **Recursos**:

  * Manipulação de sequências biológicas (DNA, RNA, proteína).
  * Tradução de DNA → proteína.
  * Leitura de arquivos **FASTA**, **GenBank** e outros formatos comuns.
  * Integração com bancos de dados biológicos (Ex: NCBI).

 **Exemplo prático:**
Traduzir uma sequência de DNA em proteína:

```python
from Bio.Seq import Seq

# Sequência de DNA (exemplo fictício)
dna_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# Tradução para proteína
protein_seq = dna_seq.translate()

print("DNA:", dna_seq)
print("Proteína:", protein_seq)
```

 **Explicação do código**:

* `Seq` cria um objeto sequência.
* `translate()` aplica a tabela de códons padrão (genética) e gera a sequência de aminoácidos.
* O resultado será algo como:

  ```
  DNA: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
  Proteína: MAIVMGR*KGAR*
  ```

  O `*` representa um códon de parada.

---

##  **2. pandas e numpy**

* **Função**: Tratamento e análise de dados tabulares e numéricos.
* **Uso em bioinformática**:

  * Trabalhar com dados de expressão gênica (**RNA-Seq**, **microarranjos**).
  * Estatísticas de alinhamentos e variantes.
  * Estruturas eficientes para manipular grandes tabelas biológicas.

 **Exemplo prático:**
Carregar dados de expressão gênica de um arquivo CSV e calcular a média de expressão:

```python
import pandas as pd
import numpy as np

# Exemplo de tabela de expressão gênica
dados = {
    "Gene": ["BRCA1", "TP53", "EGFR", "MYC"],
    "Amostra1": [120, 300, 450, 200],
    "Amostra2": [100, 280, 470, 210],
    "Amostra3": [130, 310, 460, 190]
}

df = pd.DataFrame(dados)

# Calcular a média de expressão por gene
df["Média"] = df.iloc[:, 1:].mean(axis=1)

print(df)
```

 **Explicação do código**:

* `DataFrame` cria uma tabela estruturada.
* `iloc[:, 1:]` seleciona todas as colunas a partir da segunda (amostras).
* `mean(axis=1)` calcula a média **linha a linha** (cada gene).

Saída:

```
    Gene  Amostra1  Amostra2  Amostra3   Média
0  BRCA1       120       100       130  116.67
1   TP53       300       280       310  296.67
2   EGFR       450       470       460  460.00
3    MYC       200       210       190  200.00
```

---

##  **3. matplotlib para visualização**

* **Função**: Criar gráficos científicos.
* **Uso em bioinformática**:

  * Visualizar dados de expressão gênica.
  * Histogramas de comprimento de genes.
  * Gráficos de cobertura de sequências.

 **Exemplo prático:**
Visualizar os níveis de expressão dos genes:

```python
import matplotlib.pyplot as plt

# Usando o dataframe anterior
plt.bar(df["Gene"], df["Média"], color="green")
plt.xlabel("Genes")
plt.ylabel("Expressão média")
plt.title("Níveis médios de expressão gênica")
plt.show()
```

 **Explicação do código**:

* `plt.bar` cria um gráfico de barras.
* `xlabel`, `ylabel` e `title` adicionam rótulos.
* `plt.show()` exibe o gráfico.

O resultado será um gráfico mostrando a expressão média de cada gene.

---

#  Exemplo Integrado: **Tradução de DNA + Análise + Visualização**

Agora, vamos juntar tudo em um exemplo aplicado:

1. Traduzir uma sequência de DNA em proteína.
2. Calcular a frequência de aminoácidos.
3. Visualizar os resultados em um gráfico.

```python
from Bio.Seq import Seq
import pandas as pd
import matplotlib.pyplot as plt

# Sequência de DNA
dna_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# Tradução para proteína
protein_seq = dna_seq.translate()

# Contar a frequência dos aminoácidos
freq = {}
for aa in protein_seq:
    freq[aa] = freq.get(aa, 0) + 1

# Transformar em DataFrame
df = pd.DataFrame(list(freq.items()), columns=["Aminoácido", "Frequência"])

# Visualizar em gráfico de barras
plt.bar(df["Aminoácido"], df["Frequência"], color="blue")
plt.xlabel("Aminoácidos")
plt.ylabel("Frequência")
plt.title("Frequência de aminoácidos traduzidos")
plt.show()

print("Proteína traduzida:", protein_seq)
print(df)
```

 **Resultado esperado**:

* Impressão da sequência traduzida (proteína).
* Tabela com a frequência de cada aminoácido.
* Gráfico mostrando a distribuição dos aminoácidos.

