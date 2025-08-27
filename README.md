# 📘 Algoritmos Aplicados à Biologia

Este repositório contém material para a disciplina **Algoritmos Aplicados à Biologia**, cobrindo desde conceitos básicos de programação até aplicações práticas em bioinformática.

---

## 📑 Estrutura do Curso

1. **Introdução à Programação**

   * O que é algoritmo?
   * Estruturas básicas de um programa
   * Variáveis e tipos de dados
   * Operadores (aritméticos, lógicos, relacionais)
   * Entrada e saída de dados

2. **Estruturas de Controle**

   * Condicionais (`if`, `else`, `elif`)
   * Laços de repetição (`for`, `while`)
   * Exemplos práticos: contagem de nucleotídeos em uma sequência de DNA

3. **Estruturas de Dados**

   * Listas, tuplas e dicionários
   * Strings e manipulação de texto
   * Arquivos (leitura e escrita)
   * Exemplo prático: ler arquivo FASTA e calcular frequência de bases

4. **Funções e Modularização**

   * Definição de funções
   * Escopo de variáveis
   * Importação de módulos
   * Exemplo prático: criar função para calcular GC content

5. **Bibliotecas Úteis em Bioinformática (Python)**

   * `BioPython`
   * `pandas` e `numpy`
   * `matplotlib` para visualização
   * Exemplo prático: traduzir DNA em proteína

6. **Algoritmos Clássicos em Biologia Computacional**

   * Busca de padrões em sequências (motifs)
   * Alinhamento de sequências (introdução)
   * Árvores filogenéticas (conceitos)
   * Exemplo prático: busca de ORFs em uma sequência

7. **Projetos Avançados**

   * Processamento de arquivos FASTQ
   * Estatísticas de qualidade de leitura
   * Construção de pipelines simples
   * Visualização de resultados biológicos

---

## Exemplos Práticos em Python

### Exemplo 1: Contagem de nucleotídeos em DNA

```python
dna = "ATGCGATACGCTTGA"

count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

print("Frequência de nucleotídeos:")
print("A:", count_A)
print("T:", count_T)
print("G:", count_G)
print("C:", count_C)
```

### Exemplo 2: GC Content

```python
def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq) * 100

seq = "ATGCGATACGCTTGA"
print("GC Content:", gc_content(seq), "%")
```

### Exemplo 3: Tradução DNA → Proteína (usando BioPython)

```python
from Bio.Seq import Seq

seq_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
seq_prot = seq_dna.translate()

print("DNA:", seq_dna)
print("Proteína:", seq_prot)
```

##  Objetivo

Ao final da disciplina, o estudante será capaz de:

* Entender conceitos básicos de algoritmos e programação.
* Manipular dados biológicos usando Python.
* Implementar algoritmos aplicados à biologia.
* Utilizar bibliotecas bioinformáticas para análises reais.

---

**Autor:** Prof. Allan Veras - Departamento de Bioinformática - EngBIO

**Instituição:** Universidade Federal do Pará (UFPA) - Programa de Pós-Graduação em Genética e Biologia Molecular
