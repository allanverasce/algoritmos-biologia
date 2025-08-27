# Módulo 3 – Estruturas de Dados e Arquivos 

Este módulo introduz as **estruturas de dados fundamentais do Python** (listas, tuplas e dicionários) e como utilizá-las em conjunto com a leitura e escrita de arquivos. O foco será na manipulação de **sequências biológicas** (DNA e proteínas), especialmente a partir de arquivos em formatos comuns como **TXT, CSV e FASTA**.

---

##  1. Estruturas de Dados em Python

### **Listas**

* São coleções mutáveis (podem ser modificadas).
* Usadas para armazenar sequências de elementos.

```python
# Exemplo: Lista de nucleotídeos
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

##  5. Exercício Prático: Criar tabela com frequências de nucleotídeos de todas as sequências de um FASTA

O aluno deverá escrever um programa que:

1. Leia um arquivo FASTA com várias sequências.
2. Calcule a frequência de cada nucleotídeo (A, T, G, C) por sequência.
3. Salve os resultados em um arquivo CSV.

### **Exemplo de solução:**

```python
import csv

def contar_nucleotideos(seq):
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C")
    }

with open("exemplo.fasta", "r") as f, open("frequencias.csv", "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["Sequência", "A", "T", "G", "C"])
    
    seq_id = None
    seq = ""
    
    for linha in f:
        if linha.startswith(">"):
            if seq_id and seq:
                freqs = contar_nucleotideos(seq)
                writer.writerow([seq_id, freqs["A"], freqs["T"], freqs["G"], freqs["C"]])
            seq_id = linha.strip().replace(">", "")
            seq = ""
        else:
            seq += linha.strip()
    
    # Última sequência
    if seq_id and seq:
        freqs = contar_nucleotideos(seq)
        writer.writerow([seq_id, freqs["A"], freqs["T"], freqs["G"], freqs["C"]])
```

---

##  Resultados Esperados do Módulo

Ao final, o aluno deverá ser capaz de:

* Usar listas, tuplas e dicionários para manipular dados biológicos.
* Ler e escrever arquivos em formatos comuns na bioinformática (TXT, CSV, FASTA).
* Manipular sequências de DNA/proteínas utilizando **strings em Python**.
* Calcular métricas biológicas (ex.: GC Content).
* Criar tabelas com frequências de nucleotídeos para análises comparativas.

---

Quer que eu escreva esse **mesmo módulo 3** já formatado como se fosse o **material de apostila** (com explicações teóricas + exemplos resolvidos + exercícios propostos para os alunos)?

