
# Módulo 4 – Funções e Modularização (5h)

##  Objetivos de Aprendizagem

* Compreender o que são funções em Python e como utilizá-las.
* Entender o conceito de **escopo de variáveis** (local e global).
* Aprender como reutilizar código e importar módulos.
* Aplicar funções em problemas práticos de **bioinformática**.

---

## 1. Definição de Funções em Python

Uma **função** é um bloco de código que realiza uma tarefa específica e pode ser reutilizado.
Sintaxe básica:

```python
def nome_da_funcao(parametros):
    """Documentação da função"""
    # bloco de código
    return resultado
```

Exemplo simples:

```python
def soma(a, b):
    return a + b

print(soma(3, 5))  # saída: 8
```

---

## 2. Escopo de Variáveis

O **escopo** define onde uma variável pode ser acessada.

* **Escopo local**: variáveis criadas dentro de uma função só existem dentro dela.
* **Escopo global**: variáveis criadas fora de funções podem ser acessadas em todo o programa.

Exemplo:

```python
x = 10  # variável global

def exemplo():
    x = 5  # variável local
    print("Dentro da função:", x)

exemplo()
print("Fora da função:", x)
```

Saída:

```
Dentro da função: 5
Fora da função: 10
```

---

## 3. Reuso de Código e Importação de Módulos

Podemos organizar funções em **módulos** (arquivos `.py`) e reutilizá-las em outros programas.

Exemplo: suponha que criamos um arquivo `biotools.py` com a função:

```python
# biotools.py
def gc_content(seq):
    """Calcula o conteúdo GC de uma sequência de DNA"""
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq) * 100
```

No nosso programa principal:

```python
import biotools

dna = "ATGCGCGTAA"
print("GC Content:", biotools.gc_content(dna))
```

---

## 4. Exemplo Biológico: Tradução DNA → Proteína

Podemos criar uma função que **traduz uma sequência de DNA em proteína**, utilizando o código genético.

```python
def traduzir_dna(seq):
    """Traduz uma sequência de DNA em proteína"""
    codon_table = {
        "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
        "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
        "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
        "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
        "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
        "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
        "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
        "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
        "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
        "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
        "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
        "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
        "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
        "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
        "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
        "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W",
    }
    seq = seq.upper()
    proteina = ""
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        proteina += codon_table.get(codon, "X")  # X se codon inválido
    return proteina

# Exemplo prático
dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
print(traduzir_dna(dna))
```

Saída esperada (sequência de aminoácidos):

```
MAIVMGR*KGAR*
```

---

## 5. Exercício: Identificação de ORFs (Open Reading Frames)

Um **ORF** é uma sequência de DNA que pode ser traduzida em proteína, começando em `ATG` e terminando em um códon de parada (`TAA`, `TAG`, `TGA`).

Exercício: Escreva uma função que identifique **todas as ORFs** em uma sequência de DNA.

```python
def encontrar_orfs(seq):
    """Encontra todas as ORFs em uma sequência de DNA"""
    stop_codons = ["TAA", "TAG", "TGA"]
    seq = seq.upper()
    orfs = []

    for i in range(len(seq)):
        if seq[i:i+3] == "ATG":  # início
            for j in range(i, len(seq), 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    orfs.append(seq[i:j+3])
                    break
    return orfs

# Exemplo
dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
orfs = encontrar_orfs(dna)
for i, orf in enumerate(orfs, 1):
    print(f"ORF {i}: {orf}")
```

Saída:

```
ORF 1: ATGGCCATTGTAATGGGCCGCTGA
ORF 2: ATGGGCCGCTGA
```

---

## Resumo do Módulo

* Funções permitem **organizar e reutilizar código**.
* O **escopo** controla onde variáveis existem.
* É possível criar **módulos personalizados** para análise biológica.
* Aplicações práticas incluem tradução de DNA em proteína e detecção de ORFs.

---


