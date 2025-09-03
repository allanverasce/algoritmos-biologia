# Módulo 3 – Estruturas de Dados e Arquivos 

Este módulo introduz as **estruturas de dados fundamentais do Python** (listas, tuplas e dicionários) e como utilizá-las em conjunto com a leitura e escrita de arquivos. O foco será na manipulação de **sequências biológicas** (DNA e proteínas), especialmente a partir de arquivos em formatos comuns como **TXT, CSV e FASTA**.

---

##  1. Estruturas de Dados em Python

## O que são **listas** em Python?

* **Listas** são **estruturas de dados mutáveis**, ou seja, podem ser **alteradas após a criação** (podemos adicionar, remover ou modificar elementos).
* São muito usadas quando precisamos armazenar uma **coleção de elementos** (valores, strings, números, até outras listas).
* Os itens são **ordenados**: cada elemento possui um **índice** que indica sua posição (começando do **0**).

---

## Principais características

* **Mutáveis** → podem ser modificadas depois de criadas.
* **Heterogêneas** → podem guardar diferentes tipos de dados (números, strings, objetos).
* **Dinâmicas** → podem crescer ou diminuir de tamanho (com `append()`, `remove()`, etc).

---

## Exemplo 1: Lista de nucleotídeos

```python
# Criando uma lista
nucleotideos = ["A", "T", "G", "C"]

# Acessando o primeiro elemento (índice 0)
print(nucleotideos[0])  # A

# Adicionando um elemento ao final da lista
nucleotideos.append("A")

# Exibindo a lista modificada
print(nucleotideos)  # ['A', 'T', 'G', 'C', 'A']
```

### Vamos detalhar? Veja a Explicação

1. `nucleotideos = ["A", "T", "G", "C"]` → cria uma lista com os quatro nucleotídeos básicos do DNA.
2. `nucleotideos[0]` → acessa o elemento de índice **0**, que é `"A"`.
3. `nucleotideos.append("A")` → adiciona mais um `"A"` ao final da lista.
4. `print(nucleotideos)` → exibe a lista completa já modificada.

---

##  Operações úteis com listas

* **Acessar elementos**: `lista[indice]`
* **Adicionar**: `lista.append(elemento)`
* **Inserir em posição específica**: `lista.insert(pos, elemento)`
* **Remover**: `lista.remove(elemento)` ou `lista.pop(indice)`
* **Tamanho da lista**: `len(lista)`
* **Verificar se um item está na lista**: `elemento in lista`

---

## Exemplo 2 (Biologia): Lista de genes expressos

Imagine que você tenha uma lista com os nomes de alguns **genes expressos** em um experimento.

```python
genes_expressos = ["BRCA1", "TP53", "EGFR"]

# Adicionando novos genes
genes_expressos.append("MYC")
genes_expressos.append("PTEN")

print("Lista de genes:", genes_expressos)

# Verificando se um gene está presente
if "TP53" in genes_expressos:
    print("O gene TP53 está presente na lista!")

# Removendo um gene
genes_expressos.remove("MYC")
print("Após remoção:", genes_expressos)

# Acessando um gene pelo índice
print("Primeiro gene da lista:", genes_expressos[0])
```

### Saída esperada

```
Lista de genes: ['BRCA1', 'TP53', 'EGFR', 'MYC', 'PTEN']
O gene TP53 está presente na lista!
Após remoção: ['BRCA1', 'TP53', 'EGFR', 'PTEN']
Primeiro gene da lista: BRCA1
```

## Vamos entender o passo a passo?

1. **Cria a lista inicial de genes**

```python
genes_expressos = ["BRCA1", "TP53", "EGFR"]
```

Isto define uma *lista* de strings com três elementos, na ordem dada.

2. **Adiciona novos genes ao final da lista**

```python
genes_expressos.append("MYC")
genes_expressos.append("PTEN")
```

`list.append(x)` insere o item `x` **no fim** da lista, Mega Importante isto. Depois das duas chamadas, a lista vira `["BRCA1", "TP53", "EGFR", "MYC", "PTEN"]`.

3. **Imprime a lista atual**

```python
print("Lista de genes:", genes_expressos)
```

4. **Verifica se um gene está presente**

```python
if "TP53" in genes_expressos:
    print("O gene TP53 está presente na lista!")
```

O operador de *pertinência* esta presente na LISTA ->> `in` retorna `True` se o item existir na sequência. Como `"TP53"` está na lista, a condição é verdadeira e a mensagem é impressa.

5. **Remove um gene específico**

```python
genes_expressos.remove("MYC")
print("Após remoção:", genes_expressos)
```

`list.remove(x)` **remove a primeira ocorrência** de `x` na lista. Se `x` não existir, lança `ValueError`. Aqui, `"MYC"` é removido e a lista passa a `["BRCA1", "TP53", "EGFR", "PTEN"]`. 

6. **Acessa um gene pelo índice**

```python
print("Primeiro gene da lista:", genes_expressos[0])
```
Em sequências Python, `s[i]` acessa o **i-ésimo item** começando em **0**. Logo, `genes_expressos[0]` é o primeiro elemento, `"BRCA1"`.

---


#  O que são **Tuplas** em Python?

* Uma **tupla** é uma **coleção ordenada de elementos**, muito parecida com uma **lista**.
* **Diferença principal:** **tuplas são imutáveis**, ou seja, **não podem ser alteradas após a criação**.
* Isso significa que, ao contrário das listas, você **não pode adicionar, remover ou modificar elementos** dentro de uma tupla.

Tuplas são definidas com **parênteses `()`**, enquanto listas usam colchetes `[]`.

---

##  Principais características das tuplas

1. **Imutáveis:** depois de criadas, não podem ser alteradas.
2. **Ordenadas:** cada elemento tem um índice (começando do 0).
3. **Podem armazenar tipos diferentes de dados:** números, strings, listas, etc.
4. **Mais eficientes que listas:** como não podem mudar, ocupam menos memória e são mais rápidas para acessar.
5. **Boa prática:** usar tuplas quando você quer garantir que os dados não serão modificados.

---

##  Exemplo 1: Sequência de DNA como tupla

```python
# Criando uma tupla de nucleotídeos
dna_tuple = ("A", "T", "G", "C")

# Acessando elementos por índice
print(dna_tuple[2])  # G

# Iterando sobre a tupla
for base in dna_tuple:
    print(base, end=" ")  # A T G C
```

Aqui, a tupla representa nucleotídeos fixos, que **não devem ser alterados**.

---

## Exemplo 2: Comparação entre lista e tupla

```python
# Lista (mutável)
lista_dna = ["A", "T", "G", "C"]
lista_dna.append("A")  # funciona
print(lista_dna)  # ['A', 'T', 'G', 'C', 'A']

# Tupla (imutável)
tupla_dna = ("A", "T", "G", "C")
# tupla_dna.append("A")  # ERRO! Não é permitido
```
## Dica do Allan kkkk
- Use **lista** se os dados mudam.
- Use **tupla** se os dados devem ser **fixos e protegidos**.

---

## Exemplo 3: Coordenadas de um gene (imutáveis)

Muitas vezes, em bioinformática, precisamos representar dados que **não mudam**, como **a posição de um gene em um cromossomo**.

```python
# (cromossomo, posição_inicial, posição_final, fita)
gene_coords = ("chr1", 1500, 3000, "+")

print("Gene no cromossomo:", gene_coords[0])
print("Início:", gene_coords[1])
print("Fim:", gene_coords[2])
print("Fita:", gene_coords[3])
```

Aqui, usamos uma tupla porque as coordenadas **não devem ser alteradas** durante a análise.

---

## Exemplo 4: Uso de tupla para retorno de função

Funções podem retornar múltiplos valores em forma de tupla.

```python
def estatisticas_dna(seq):
    return (seq.count("A"), seq.count("T"), seq.count("G"), seq.count("C"))

dna = "ATGCGATATG"
contagem = estatisticas_dna(dna)

print("Contagem (A, T, G, C):", contagem)
```

Saída Esperada:

```
Contagem (A, T, G, C): (3, 3, 2, 2)
```

---

# Resumindo

* **Listas (`[]`)** → mutáveis, ideais para dados que mudam.
* **Tuplas (`()`)** → imutáveis, ideais para dados **fixos**.
* Em **biologia**, tuplas podem representar coisas como:

  * **Coordenadas fixas** de genes.
  * **Pares de bases** ou **motivos conservados**.
  * **Resultados imutáveis** de funções (como contagens de nucleotídeos).

---

#  O que são **Dicionários** em Python?

* Um **dicionário** é uma estrutura de dados que **armazenada pares chave–valor**.
* A ideia é: cada **chave** funciona como um "rótulo" que aponta para um **valor** associado.
* Sintaxe: `{chave: valor, chave: valor, ...}`

 Diferente de listas e tuplas (que acessamos pelo índice), nos dicionários acessamos os elementos pela **chave**.

---

## Características importantes

1. **Chaves únicas:** cada chave aparece apenas uma vez.
2. **Valores podem se repetir:** mas a chave não.
3. **Mutáveis:** podemos adicionar, remover ou alterar elementos.
4. **Muito úteis em bioinformática** → porque podemos mapear **genes, nucleotídeos, proteínas, contagens, anotações, etc.**

---

##  Exemplo 1: Frequência de nucleotídeos

```python
freq = {"A": 10, "T": 5, "G": 8, "C": 7}

print("Frequência de A:", freq["A"])  # 10

# Alterando valores
freq["T"] = 6
print("Nova frequência de T:", freq["T"])  # 6

# Adicionando chave nova
freq["N"] = 2
print(freq)
```
Esse dicionário associa cada nucleotídeo à sua contagem em uma sequência.

---

## Exemplo 2: Frequência de nucleotídeos em uma sequência de DNA

```python
dna = "ATGCGATATGCGAAA"

# Criando um dicionário vazio
freq = {}

for base in dna:
    if base in freq:
        freq[base] += 1  # soma +1 se a base já existir
    else:
        freq[base] = 1   # cria a chave se ainda não existir

print("Frequência de nucleotídeos:", freq)
```

Saída esperada (Nota : pode variar dependendo da sequência):

```
Frequência de nucleotídeos: {'A': 6, 'T': 3, 'G': 3, 'C': 3}
```

---

##  Exemplo 3: Mapeando genes a funções

Um dicionário pode relacionar **genes** aos seus **papéis biológicos**.

```python
genes = {
    "BRCA1": "Reparo de DNA",
    "TP53": "Supressor tumoral",
    "EGFR": "Receptor de crescimento celular",
    "MYC": "Regulação da transcrição"
}

print("Função do TP53:", genes["TP53"])
```

Saída Esperada:

```
Função do TP53: Supressor tumoral
```

---

##  Exemplo 4: Posições de um motivo em uma sequência

Um dicionário pode guardar a posição de um **motivo de DNA**.

```python
dna = "ATGCGATGATGTAG"
motivo = "ATG"
posicoes = {}

for i in range(len(dna) - len(motivo) + 1):
    if dna[i:i+len(motivo)] == motivo:
        posicoes[i] = motivo

print("Posições do motivo:", posicoes)
```

Saída esperada:

```
Posições do motivo: {0: 'ATG', 5: 'ATG', 8: 'ATG'}
```

---

## Exemplo 5: Dicionário aninhado (genes e expressão)

Dicionários podem conter **outros dicionários**, representando dados mais complexos.

```python
expressao_genica = {
    "BRCA1": {"condição_controle": 50, "condição_tratamento": 80},
    "TP53": {"condição_controle": 70, "condição_tratamento": 65},
    "EGFR": {"condição_controle": 40, "condição_tratamento": 100}
}

# Acessando valores específicos
print("Expressão de BRCA1 no tratamento:", expressao_genica["BRCA1"]["condição_tratamento"])
```

 Saída:

```
Expressão de BRCA1 no tratamento: 80
```

---

##  Exemplo 6: Tradução de DNA → aminoácidos

Um dicionário pode guardar o **código genético**.

```python
codon_table = {
    "ATG": "Met", "TGG": "Trp",
    "TAA": "Stop", "TAG": "Stop", "TGA": "Stop"
}

print("Códon ATG traduz para:", codon_table["ATG"])
```

Saída esperada:

```
Códon ATG traduz para: Met
```

---

#  Resumindo

* **Dicionários** armazenam **pares chave–valor**.
* São ideais para dados que possuem **identificadores únicos** (genes, códons, nucleotídeos, proteínas).
* Em **biologia**, podem ser usados para:

  * Contar nucleotídeos ou aminoácidos.
  * Mapear genes para funções ou níveis de expressão.
  * Guardar tabelas como o **código genético**.
  * Armazenar **resultados de análises** (frequências, posições, anotações).

---

#  Leitura e Escrita de Arquivos em Python

Em Python usamos a função **`open()`** para abrir arquivos.
A sintaxe geral é:

```python
with open("nome_arquivo.txt", "modo") as f:
    # operações no arquivo
```

* `"w"` → modo **escrita** (cria/reescreve o arquivo).
* `"r"` → modo **leitura**.
* `"a"` → modo **append** (adiciona ao final).

O uso do **`with`** é importante porque garante que o arquivo seja **fechado automaticamente** ao final, evitando erros.

---

##  1. Arquivos **TXT**

São arquivos de texto simples, muito usados para guardar uma sequência ou resultados curtos.

###  Exemplo: Escrever e ler uma sequência de DNA

```python
# Escrevendo em um arquivo TXT
with open("sequencia.txt", "w") as f:
    f.write("ATGCGTA")

# Lendo do arquivo TXT
with open("sequencia.txt", "r") as f:
    seq = f.read()

print("Sequência lida:", seq)
```

###  Explicação:

1. O programa cria o arquivo `sequencia.txt` e escreve a string `"ATGCGTA"`.
2. Depois, abre o arquivo em modo leitura (`"r"`) e lê todo o conteúdo com `.read()`.
3. O resultado é exibido no terminal.

 Saída:

```
Sequência lida: ATGCGTA
```

 Uso em biologia: salvar **sequências individuais** ou **resultados curtos** de análises.

---

##  2. Arquivos **CSV**

* CSV significa **Comma-Separated Values** (valores separados por vírgula).
* É muito usado para **tabelas de resultados**, por exemplo, contagem de nucleotídeos em várias sequências.
* Python tem a biblioteca `csv` que facilita a manipulação.

###  Exemplo: Frequência GC em diferentes sequências

```python
import csv

# Escrevendo CSV
with open("resultados.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sequência", "GC_Content"])  # Cabeçalho
    writer.writerow(["Seq1", 0.55])
    writer.writerow(["Seq2", 0.62])

# Lendo CSV
with open("resultados.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

###  Explicação:

1. Criamos o arquivo `resultados.csv`.
2. `writer.writerow([...])` escreve uma linha no arquivo (pode ser cabeçalho ou dados).
3. Ao ler o arquivo, usamos `csv.reader(f)` para iterar pelas linhas.

 Saída:

```
['Sequência', 'GC_Content']
['Seq1', '0.55']
['Seq2', '0.62']
```

 Uso em biologia: armazenar **tabelas de frequências**, **níveis de expressão gênica**, **resultados de análises em várias amostras**.

---

##  3. Arquivos **FASTA**

* Formato padrão em **bioinformática** para armazenar sequências de DNA, RNA ou proteínas.
* Estrutura:

  ```
  >identificador_da_sequência
  ATGCGTAGCTA...
  ```
* Cada sequência começa com uma linha de cabeçalho (`>`), seguida pela sequência.

###  Exemplo: Leitura simples de FASTA

```python
# Exemplo de leitura de um arquivo FASTA
with open("exemplo.fasta", "r") as f:
    for linha in f:
        if not linha.startswith(">"):  # Ignora cabeçalhos
            seq = linha.strip()        # Remove espaços e quebras de linha
            print(seq)
```

###  Explicação:

1. Abre o arquivo `exemplo.fasta`.
2. Percorre cada linha.
3. Se a linha **não começar com `>`**, significa que é sequência (não cabeçalho).
4. Exibe a sequência.

Exemplo de entrada (`exemplo.fasta`):

```
>seq1
ATGCGTA
>seq2
TTGCAAGT
```

Saída esperada:

```
ATGCGTA
TTGCAAGT
```

 Uso em biologia: manipular **sequências reais** de DNA/proteína.

---

#  Resumindo

| Formato   | Uso principal                                            | Exemplo em Biologia                     |
| --------- | -------------------------------------------------------- | --------------------------------------- |
| **TXT**   | Texto simples, sequências pequenas ou resultados rápidos | Guardar uma sequência de DNA            |
| **CSV**   | Tabelas de dados, fácil de abrir no Excel                | Tabela de frequências, expressão gênica |
| **FASTA** | Padrão bioinformática, sequências biológicas             | Genomas, genes, proteínas               |

---

**Conclusão:**

* Use **TXT** para informações simples.
* Use **CSV** para tabelas e resultados comparativos.
* Use **FASTA** para **sequências biológicas**, pois é padrão universal em bioinformática.

---


## 3. Manipulação de Sequências Biológicas com Strings

Strings em Python podem ser tratadas como listas de caracteres, o que facilita a manipulação de DNA e proteínas.

```python
dna = "ATGCGTAC"
print(dna[0])      # A
print(len(dna))    # 8
print(dna.count("G"))  # 2
print(dna.replace("T", "U"))  # AUGCGUAC (RNA)
```

---

##  4. Exemplo Biológico: Ler arquivo FASTA e calcular **GC Content**

O **GC Content** é a porcentagem de bases **Guanina (G) + Citosina (C)** em uma sequência de DNA.

```python
def gc_content(seq):
    """Calcula o GC content de uma sequência de DNA"""
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq)

with open("exemplo.fasta", "r") as f:
    for linha in f:
        if not linha.startswith(">"):
            seq = linha.strip()
            print("Sequência:", seq)
            print("GC Content:", gc_content(seq))
```

---

##  5. Vamos praticar? Sua tarefa é: Criar tabela com frequências de nucleotídeos de todas as sequências de um FASTA

O aluno deverá escrever um programa que:

1. Leia um arquivo FASTA com várias sequências.
2. Calcule a frequência de cada nucleotídeo (A, T, G, C) por sequência.
3. Salve os resultados em um arquivo CSV.


---

##  Resultados Esperados do Módulo

Ao final, o aluno deverá ser capaz de:

* Usar listas, tuplas e dicionários para manipular dados biológicos.
* Ler e escrever arquivos em formatos comuns na bioinformática (TXT, CSV, FASTA).
* Manipular sequências de DNA/proteínas utilizando **strings em Python**.
* Calcular métricas biológicas (ex.: GC Content).
* Criar tabelas com frequências de nucleotídeos para análises comparativas.

---


