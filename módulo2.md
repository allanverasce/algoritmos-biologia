# Módulo 2 – Estruturas de Controle

## Objetivos de Aprendizagem
- Entender como funcionam estruturas condicionais (`if`, `else`, `elif`) em Python.
- Compreender e aplicar laços de repetição (`for`, `while`).
- Usar estruturas de controle para resolver problemas em bioinformática.
- Implementar exemplos práticos para análise de sequências biológicas.

---

## 1. Estruturas Condicionais

As **estruturas condicionais** permitem que o programa **tome decisões** dependendo de certas condições.

### Sintaxe
```
if condição:
    # bloco se condição for verdadeira
elif outra_condição:
    # bloco se a primeira for falsa e esta for verdadeira
else:
    # bloco se todas as condições forem falsas
```
Exemplo de utilização

```
idade = 20

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 60:
    print("Adulto")
else:
    print("Idoso")
```

## 2. Estruturas de Repetição (Loops)

Os loops permitem que um bloco de código seja repetido várias vezes.

**2.1 for**

Usado quando sabemos quantas vezes queremos repetir.

```
for i in range(5):
    print("Repetição número:", i)
```
Exemplo Biológico 1: Percorrer uma sequência de DNA

```
dna = "ATGCGT"

for base in dna:
    print("Base encontrada:", base)
```

**2.2 while**

Usado quando queremos repetir até que uma condição seja falsa.

```
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

## 3. Exemplos de Aplicações em Biologia
**Exemplo Biológico 1:** </br>
As estruturas de controle são úteis, por exemplo, para analisar sequências de DNA, buscar motivos ou percorrer listas de genes.

```
dna = "ATGCGATACGTAGCGTAGC"
motivo = "ATG"

if motivo in dna:
    print("Motivo encontrado na sequência!")
else:
    print("Motivo não encontrado.")
```

**Exemplo Biológico 2:**
```
dna = "ATGCGATACGTAGCGTAGC"

for base in dna:
    print(base)
```

**Exemplo Biológico 3:**
Vamos melhorar esse exemplo? ->  Procurando todas as ocorrências de um motivo
```
dna = "ATGCGATGATGTAG"
motivo = "ATG"
posicoes = []

for i in range(len(dna) - len(motivo) + 1):
    if dna[i:i+len(motivo)] == motivo:
        posicoes.append(i)

print("Motivo encontrado nas posições:", posicoes)
```
Beleza, Allan 👌 Vou explicar passo a passo esse código em Python, que busca um **motivo** (padrão de sequência) dentro de uma string de DNA.

---

### 🔹 O código

```python
dna = "ATGCGATGATGTAG"
motivo = "ATG"
posicoes = []

for i in range(len(dna) - len(motivo) + 1):
    if dna[i:i+len(motivo)] == motivo:
        posicoes.append(i)

print("Motivo encontrado nas posições:", posicoes)
```

---

### Vamos Enteder! Veja a explicação passo a passo

1. **Definição da sequência de DNA e do motivo**

   ```python
   dna = "ATGCGATGATGTAG"
   motivo = "ATG"
   ```

   Aqui temos uma string representando o DNA (`dna`) e o **motivo** que queremos procurar (`ATG`).

2. **Lista para armazenar posições**

   ```python
   posicoes = []
   ```

   Essa lista guardará os **índices** onde o motivo aparece dentro da sequência.

3. **Laço `for` para percorrer a sequência**

   ```python
   for i in range(len(dna) - len(motivo) + 1):
   ```

   * `len(dna)` → comprimento da sequência (aqui, 14).
   * `len(motivo)` → comprimento do motivo (aqui, 3).
   * Subtraímos `len(motivo) - 1` porque não faz sentido começar a verificar quando não há espaço suficiente para caber o motivo.
    Assim, o loop percorre todos os **pontos possíveis de início** do motivo dentro da sequência.

4. **Verificação se o trecho é igual ao motivo**

   ```python
   if dna[i:i+len(motivo)] == motivo:
   ```

   * `dna[i:i+len(motivo)]` pega um **fatiamento** (slice) da sequência, começando na posição `i` e indo até `i+3`.
   * Se esse trecho for igual ao motivo, encontramos uma ocorrência.

5. **Armazenando a posição**

   ```python
   posicoes.append(i)
   ```

   Se encontrou, guarda a posição inicial (`i`) na lista.

6. **Resultado final**

   ```python
   print("Motivo encontrado nas posições:", posicoes)
   ```

   Exibe a lista com todas as posições.
   Para esse exemplo, a saída será:

   ```
   Motivo encontrado nas posições: [0, 5, 8]
   ```

   Isso significa que o motivo **"ATG"** aparece nas posições **0, 5 e 8** da string.

---

## 4. Vamos treinar? --> Exercício Prático

A sua tarefa: Escreva um programa que:

- Peça ao usuário uma sequência de DNA.
- Peça um motivo (substring) para buscar.
- Informe todas as posições onde o motivo ocorre.
- Se o motivo não existir, exiba mensagem apropriada.


## Resumo do Módulo

- Condicionais (if/else/elif) permitem que programas tomem decisões.
- Loops (for e while) permitem repetir instruções.
- Estruturas de controle são essenciais para análise de sequências biológicas.
- Aplicação prática: buscar motivos (como códons ou padrões) em sequências de DNA.
