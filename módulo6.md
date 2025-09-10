#  Criação de Módulos em Python e Uso em Outros Scripts

##  O que é um módulo?

* Em Python, **módulo** é simplesmente um **arquivo com extensão `.py`** que contém código (funções, classes, variáveis) que você deseja **reutilizar** em outros scripts.
* Em vez de escrever o mesmo código várias vezes, você o coloca em um módulo e depois **importa** em outros programas.

 **Analogia biológica**:
Pense em um módulo como um **gene**. Ele contém instruções específicas (funções).
Quando importamos o módulo em outro script, é como se estivéssemos **expressando esse gene** em uma célula diferente (programa).

---

##  Como criar um módulo

### Exemplo simples

 Arquivo: **`meu_modulo.py`**

```python
# Definição de funções matemáticas
def soma(a, b):
    return a + b

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)
```

Esse arquivo é um **módulo**. Ele define duas funções (`soma` e `fatorial`) que podem ser importadas em outros scripts.

---

##  Como importar um módulo

### Arquivo: **`main.py`**

```python
import meu_modulo

print("Soma:", meu_modulo.soma(5, 7))
print("Fatorial:", meu_modulo.fatorial(5))
```

### Saída:

```
Soma: 12
Fatorial: 120
```

### Outras formas de importação

* Importar apenas funções específicas:

  ```python
  from meu_modulo import soma
  print(soma(10, 20))
  ```
* Importar com apelido (mais curto):

  ```python
  import meu_modulo as mm
  print(mm.fatorial(6))
  ```
* Importar tudo (menos recomendado):

  ```python
  from meu_modulo import *
  ```

---

#  Exemplo aplicado à Biologia

Agora, vamos criar um **módulo biológico** com funções úteis em bioinformática.

###  Arquivo: **`bio_utils.py`**

```python
from Bio.Seq import Seq

# Função para calcular o conteúdo GC
def gc_content(seq):
    seq = seq.upper()
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq) * 100

# Função para traduzir DNA em proteína
def traduzir(seq):
    dna = Seq(seq)
    return dna.translate()

# Função para gerar a sequência reversa complementar
def reversa_complementar(seq):
    dna = Seq(seq)
    return dna.reverse_complement()
```

Esse módulo (`bio_utils.py`) contém **funções úteis para análises de sequências**.

---

###  Arquivo: **`analise.py`**

```python
import bio_utils

# Exemplo de sequência de DNA
dna_seq = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

# Usando as funções do módulo
print("Sequência de DNA:", dna_seq)
print("GC Content:", bio_utils.gc_content(dna_seq), "%")
print("Proteína traduzida:", bio_utils.traduzir(dna_seq))
print("Reversa complementar:", bio_utils.reversa_complementar(dna_seq))
```

### Saída esperada:

```
Sequência de DNA: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
GC Content: 56.41 %
Proteína traduzida: MAIVMGR*KGAR*
Reversa complementar: CTATCGGGCACCCTTTCAGCGGCCCATTACAATGGCCAT
```

---

#  Explicação detalhada do exemplo biológico

1. **GC Content**:

   * Mede a proporção de nucleotídeos **Guanina (G)** e **Citosina (C)** em relação ao total da sequência.
   * Importante para identificar estabilidade de regiões genômicas, regiões promotoras e diferenças entre organismos.

2. **Tradução DNA → Proteína**:

   * Usa a tabela de códons padrão.
   * Cada trinca de nucleotídeos (códon) é convertida em um aminoácido.
   * O `*` representa um códon de parada.

3. **Sequência Reversa Complementar**:

   * Importante em bioinformática porque o DNA é fita dupla.
   * Muitas vezes precisamos analisar a fita complementar para identificar genes em sentido reverso.

---

# Vantagens de usar módulos em projetos de Bioinformática

* **Organização**: facilita dividir o código em partes lógicas (ex: leitura de FASTA, análises de sequências, visualização de dados).
* **Reutilização**: você pode usar o mesmo módulo em diferentes projetos.
* **Colaboração**: outros pesquisadores podem importar e usar suas funções sem precisar entender todo o código.
* **Escalabilidade**: em projetos maiores, você pode transformar módulos em **pacotes** (com várias pastas e arquivos organizados).

---


