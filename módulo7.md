# Algoritmo 1: Alinhamento Simples (Needleman–Wunsch)

Imagine que temos duas sequências de DNA:

```
Seq1 = "GATTACA"
Seq2 = "GCATGCU"
```

A pergunta é: **quão parecidas elas são, o que você acha?**

Para tentar resolver isso, vamos construir uma **matriz de comparação**, onde cada posição mostra **o melhor score até ali**.

---

## 2. Regras do alinhamento

1. **Pontuação simples:** Vale salientar que os algoritmos utilizam métricas próprias, aqui temos apenas um exemplo.

   * Igualdade (match): +1
   * Diferença (mismatch): -1
   * Gap (`-`): -1

2. **Construção da matriz:**

   * Linhas = uma sequência
   * Colunas = outra sequência
   * Primeira linha e primeira coluna começam com penalidades acumuladas de gap.

---

## 3. Passo Visual (exemplo de como ela fica)

```
      -   G   C   A   T   G   C   U
  -   0  -1  -2  -3  -4  -5  -6  -7
  G  -1
  A  -2
  T  -3
  T  -4
  A  -5
  C  -6
  A  -7
```

O lance aqui é preencher **célula por célula**, sempre pegando o **máximo** entre:

* Diagonal (match/mismatch)
* Esquerda (gap)
* Cima (gap)

---

## 4. Implementação Simples em Python

Neste exemplo, fazemos **só a matriz de score**, sem reconstruir o alinhamento.

```python
# Needleman-Wunsch simplificado (apenas score final)

# Sequências de exemplo
seq1 = "GATTACA"
seq2 = "GCATGCU"

# Regras de pontuação
match = 1
mismatch = -1
gap = -1

# Criar matriz (linhas = len(seq1)+1, colunas = len(seq2)+1)
n = len(seq1) + 1
m = len(seq2) + 1
matriz = [[0] * m for _ in range(n)]

# Inicializar primeira linha e coluna com penalidade de gaps
for i in range(n):
    matriz[i][0] = i * gap
for j in range(m):
    matriz[0][j] = j * gap

# Preencher a matriz
for i in range(1, n):
    for j in range(1, m):
        if seq1[i-1] == seq2[j-1]:
            score_diag = matriz[i-1][j-1] + match
        else:
            score_diag = matriz[i-1][j-1] + mismatch
        
        score_cima = matriz[i-1][j] + gap
        score_esq = matriz[i][j-1] + gap
        
        matriz[i][j] = max(score_diag, score_cima, score_esq)

# Mostrar matriz
print("Matriz de pontuação:")
for linha in matriz:
    print(linha)

print("\nScore final do alinhamento:", matriz[-1][-1])
```

---

## 5. Saída esperada (resumida)

A matriz será preenchida com números mostrando os **melhores scores acumulados**.
No final, o **último valor da matriz** é o **score do melhor alinhamento global**.

Exemplo:

```
Matriz de pontuação:
[0, -1, -2, -3, -4, -5, -6, -7]
[-1, 1, 0, -1, -2, -3, -4, -5]
[-2, 0, 0, 1, 0, -1, -2, -3]
...

Score final do alinhamento: 0
```

---

Se mudarmos os pesos (por exemplo, gap = -2 em vez de -1), como o alinhamento final muda, testa ai?

---


# Algoritmo 2: Guloso para Montagem 

Imagine que temos estas **reads curtas** de uma sequência de DNA:

```
Read1 = "ATTAGAC"
Read2 = "GACCTT"
Read3 = "AGACCT"
Read4 = "CCTTGA"
```

* Cada read é como **uma peça de quebra-cabeça**.
* Nosso objetivo: **montar a sequência original**, colando as reads que se **sobrepõem**.
* Desafio: **não sabemos a ordem das reads**; precisamos encontrar sobreposições máximas.

---

## 2. Ideia do algoritmo guloso

* **Passo 1:** procurar **duas reads com maior sobreposição**.
* **Passo 2:** unir essas duas reads em uma única sequência.
* **Passo 3:** repetir o processo com as demais reads até que todas estejam coladas.

 “Guloso” significa que **sempre escolhemos a melhor escolha no momento**, sem olhar todas as combinações possíveis.

---

## 3. Exemplo visual

1. Identificar sobreposição máxima:

```
Read1: ATTAGAC
Read3: AGACCT
```

* Sobreposição: `"AGAC"`
* Junta: `"ATTAGACCT"`

2. Próxima sobreposição:

```
ATTAGACCT
Read2: GACCTT
```

* Sobreposição: `"GACCT"`
* Junta: `"ATTAGACCTT"`

3. Última read:

```
ATTAGACCTT
Read4: CCTTGA
```

* Sobreposição: `"CCTT"`
* Junta: `"ATTAGACCTTGA"` --> Sequência montada.

---

## 4. Implementação em Python (Exemplo apenas kkk)

```python
# Algoritmo guloso de montagem de genomas
reads = ["ATTAGAC", "GACCTT", "AGACCT", "CCTTGA"]

def overlap(a, b):
    """Retorna o tamanho máximo de sobreposição entre a final de 'a' e início de 'b'"""
    max_ov = 0
    min_len = min(len(a), len(b))
    for i in range(1, min_len + 1):
        if a[-i:] == b[:i]:
            max_ov = i
    return max_ov

def greedy_assemble(reads):
    reads = reads.copy()
    while len(reads) > 1:
        max_ov = -1
        best_pair = (0, 1)
        merged_seq = ""
        # Procurar par com maior sobreposição
        for i in range(len(reads)):
            for j in range(len(reads)):
                if i != j:
                    ov = overlap(reads[i], reads[j])
                    if ov > max_ov:
                        max_ov = ov
                        best_pair = (i, j)
                        merged_seq = reads[i] + reads[j][ov:]
        # Substituir reads pelo merge
        i, j = best_pair
        reads[i] = merged_seq
        reads.pop(j if j < i else j)
    return reads[0]

# Testar
assembled = greedy_assemble(reads)
print("Sequência montada:", assembled)
```

---

## 5. Saída esperada

```
Sequência montada: ATTAGACCTTGA
```

* Observe que **o algoritmo escolheu sempre a maior sobreposição** disponível.
* É **simples, mas rápido** — ideal para explicar a ideia aos iniciantes.

---

## 6. Pontos importantes 

* O algoritmo guloso **não garante sempre a montagem correta** se houver múltiplas sobreposições com mesmo tamanho.
* Ele é uma **introdução conceitual**, mas genomas reais requerem algoritmos mais sofisticados (SPAdes, Velvet, etc.).
---

# Algoritmo 3: Busca Binária em Genes 

* Bancos de genes podem ter **milhares ou milhões de entradas**.

* Se procurássemos **sequencialmente**, levando um gene por vez, seria **muito lento**.

* Exemplo:

  ```
  genes = ["BRCA1", "CFTR", "HBB", "TP53"]
  ```

  * Se quisermos encontrar `"TP53"`, procurar elemento por elemento funciona aqui, mas **não escala** para milhares de genes.

* **Solução:** usar **busca binária**, que corta a lista ao meio a cada passo, encontrando o gene rapidamente.

---

## 2. Ideia da busca binária

1. Lista precisa estar **ordenada**.
2. Comparar o **alvo** com o elemento do **meio** da lista.
3. Três possibilidades:

   * Igual → encontramos o gene 
   * Alvo > meio → procurar **metade direita** da lista
   * Alvo < meio → procurar **metade esquerda** da lista
4. Repetir até encontrar ou a lista acabar.

**Analogia:** procurar uma palavra em um dicionário. 

---

## 3. Implementação em Python (simples)

```python
# Lista de genes
genes = ["BRCA1", "CFTR", "HBB", "TP53"]

# Ordenar a lista
genes.sort()  # ['BRCA1', 'CFTR', 'HBB', 'TP53']

# Função de busca binária
def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio  # Encontrou
        elif lista[meio] < alvo:
            inicio = meio + 1  # Buscar na metade direita
        else:
            fim = meio - 1  # Buscar na metade esquerda
    return -1  # Não encontrou

# Teste
indice = busca_binaria(genes, "TP53")
print("Índice de TP53:", indice)
```

**Saída esperada:**

```
Índice de TP53: 3
```

---

## 4. Atividade prática para os alunos (10 min)

1. Pedir que adicionem novos genes à lista:

```python
genes += ["MYC", "EGFR", "VEGFA"]
```

2. Ordenar a lista novamente:

```python
genes.sort()
```

3. Testar a busca binária para encontrar diferentes genes, por exemplo:

```python
print(busca_binaria(genes, "EGFR"))
print(busca_binaria(genes, "BRCA1"))
```


### Resumo

* **Busca binária** é eficiente e funciona **apenas em listas ordenadas**.
* Reduz drasticamente o número de comparações necessárias.
* Muito usada em bioinformática para **procurar genes, proteínas ou sequências específicas em grandes bancos de dados**.
---






