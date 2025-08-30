# Módulo 3 – Estruturas de Dados e Arquivos 

Este módulo introduz as **estruturas de dados fundamentais do Python** (listas, tuplas e dicionários) e como utilizá-las em conjunto com a leitura e escrita de arquivos. O foco será na manipulação de **sequências biológicas** (DNA e proteínas), especialmente a partir de arquivos em formatos comuns como **TXT, CSV e FASTA**.

---

##  1. Estruturas de Dados em Python

## O que são **listas** em Python?

* **Listas** são **estruturas de dados mutáveis**, ou seja, podem ser **alteradas após a criação** (podemos adicionar, remover ou modificar elementos).
* São muito usadas quando precisamos armazenar uma **coleção de elementos** (valores, strings, números, até outras listas).
* Os itens são **ordenados**: cada elemento possui um **índice** que indica sua posição (começando do **0**).

---

## 🔹 Principais características

* **Mutáveis** → podem ser modificadas depois de criadas.
* **Heterogêneas** → podem guardar diferentes tipos de dados (números, strings, objetos).
* **Dinâmicas** → podem crescer ou diminuir de tamanho (com `append()`, `remove()`, etc).

---

## 🔹 Exemplo 1: Lista de nucleotídeos

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

## 🔹 Operações úteis com listas

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

## Exemplo 3 (Biologia): Exemplo: Lista de nucleotídeos
```python
nucleotideos = ["A", "T", "G", "C"]
print(nucleotideos[0])  # A
nucleotideos.append("A")
print(nucleotideos)
```

### **Tuplas**

* São imutáveis (não podem ser alteradas após a criação).
* Úteis para armazenar dados que não devem mudar.

```python
# Exemplo: Uma sequência de DNA imutável
dna_tuple = ("A", "T", "G", "C")
print(dna_tuple[2])  # G
```

### **Dicionários**

* Armazenam pares chave-valor.
* Muito úteis para representar **contagens de nucleotídeos** ou **mapeamentos de genes**.

```python
# Exemplo: Frequência de nucleotídeos
freq = {"A": 10, "T": 5, "G": 8, "C": 7}
print(freq["A"])  # 10
```

---

## 2. Leitura e Escrita de Arquivos

### **Arquivos TXT**

```python
# Escrevendo em um TXT
with open("sequencia.txt", "w") as f:
    f.write("ATGCGTA")

# Lendo o TXT
with open("sequencia.txt", "r") as f:
    seq = f.read()
print(seq)
```

### **Arquivos CSV**

Úteis para tabelas de resultados (ex.: contagem de nucleotídeos em várias sequências).

```python
import csv

# Escrevendo CSV
with open("resultados.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sequência", "GC_Content"])
    writer.writerow(["Seq1", 0.55])
    writer.writerow(["Seq2", 0.62])

# Lendo CSV
with open("resultados.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### **Arquivos FASTA**

Formato padrão em bioinformática para armazenar sequências.

```python
# Exemplo de leitura simples de um FASTA
with open("exemplo.fasta", "r") as f:
    for linha in f:
        if not linha.startswith(">"):  # Ignora cabeçalhos
            seq = linha.strip()
            print(seq)
```

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


