# Módulo 1 – Fundamentos de Programação

## Objetivos de Aprendizagem
- Compreender o que é um algoritmo.
- Aprender a usar variáveis, tipos de dados e operadores em Python.
- Usar entrada/saída de dados.
- Manipular strings.
- Aplicar esses conceitos em exemplos práticos de biologia.

---

## 1. O que é um Algoritmo?

Um **algoritmo** é um conjunto de instruções bem definidas, finitas e ordenadas que resolvem um problema ou realizam uma tarefa.

👉 Exemplos simples de algoritmos no cotidiano:
- Receita de bolo (passo a passo).
- Instruções para ligar um computador.
- Protocolo de laboratório.

### Exemplo em Pseudocódigo
Encontrar o maior de dois números:

```
início
ler A
ler B
se A > B então
escreva "A é maior"
senão
escreva "B é maior"
fim
```
---

## 2. Variáveis, Tipos de Dados e Operadores em Python

Uma **variável** é um espaço na memória usado para armazenar informações.

### Tipos básicos em Python
- `int` → números inteiros
- `float` → números decimais
- `str` → texto (strings)
- `bool` → valores lógicos (True/False)

### Exemplo em Python

```
idade = 25       # inteiro
altura = 1.75    # float
nome = "Ana"     # string
cientista = True # booleano

print(idade, altura, nome, cientista)
```

Operadores
- Aritméticos: + - * / % ** //
- Relacionais: == != > < >= <=
- Lógicos: and, or, not

```
a = 10
b = 3
print("Soma:", a + b)
print("Divisão inteira:", a // b)
print("Potência:", a ** b)
print("Comparação:", a > b)
```

##  **Operadores Aritméticos**

São usados para realizar cálculos matemáticos.

* **`+` (adição):** soma valores.

  ```python
  print(5 + 3)  # 8
  ```

* **`-` (subtração):** subtrai valores.

  ```python
  print(10 - 4)  # 6
  ```

* **`*` (multiplicação):** multiplica valores.

  ```python
  print(7 * 2)  # 14
  ```

* **`/` (divisão):** divide valores, sempre retorna número decimal (float).

  ```python
  print(10 / 3)  # 3.333...
  ```

* **`%` (módulo):** retorna o resto da divisão.

  ```python
  print(10 % 3)  # 1
  ```

* **`**` (exponenciação):** potência.

  ```python
  print(2 ** 3)  # 8
  ```

* **`//` (divisão inteira):** retorna apenas a parte inteira da divisão.

  ```python
  print(10 // 3)  # 3
  ```

---

## **Operadores Relacionais**

São usados para comparar valores. O resultado é sempre **True** (verdadeiro) ou **False** (falso).

* **`==` (igualdade):** verifica se dois valores são iguais.

  ```python
  print(5 == 5)  # True
  ```

* **`!=` (diferente):** verifica se dois valores são diferentes.

  ```python
  print(5 != 3)  # True
  ```

* **`>` (maior que):**

  ```python
  print(10 > 7)  # True
  ```

* **`<` (menor que):**

  ```python
  print(3 < 8)  # True
  ```

* **`>=` (maior ou igual a):**

  ```python
  print(5 >= 5)  # True
  ```

* **`<=` (menor ou igual a):**

  ```python
  print(4 <= 2)  # False
  ```

---

## **Operadores Lógicos**

Usados para combinar condições.

* **`and` (e):** retorna **True** apenas se **todas** as condições forem verdadeiras.

  ```python
  print(5 > 2 and 10 > 5)  # True
  ```

* **`or` (ou):** retorna **True** se **pelo menos uma** condição for verdadeira.

  ```python
  print(5 > 10 or 3 < 8)  # True
  ```

* **`not` (não):** inverte o valor lógico.

  ```python
  print(not (5 > 2))  # False
  ```

---

## Mais exemplos de funções Matemáticas

Python possui funções matemáticas embutidas e também a biblioteca math para cálculos mais avançados.

Função	Descrição	Exemplo
- round(x, n)	Arredonda número para n casas decimais	round(3.14159, 2) → 3.14
- abs(x)	Retorna o valor absoluto	abs(-10) → 10
- pow(x, y) ou x ** y	Potência	pow(2,3) → 8
- max(a, b, c)	Maior valor	max(4,7,2) → 7
- min(a, b, c)	Menor valor	min(4,7,2) → 2

Para usar a biblioteca math é necessário fazer o import, veja o exemplo:

```
import math

print("Raiz quadrada:", math.sqrt(16))
print("Número pi:", math.pi)
print("Logaritmo natural de 10:", math.log(10))
print("Seno de 90°:", math.sin(math.radians(90)))
```

Em resumo:

* **Aritméticos** → fazem contas.
* **Relacionais** → comparam valores.
* **Lógicos** → combinam condições para decisões.

---

## 3. Entrada e Saída de Dados

Em Python usamos:

- input() → entrada do usuário
- print() → saída no console
Exemplo

```
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("Olá,", nome, "! Você tem", idade, "anos.")
```
## 4. Manipulação de Strings

Strings são fundamentais em bioinformática porque sequências de DNA, RNA e proteínas são representadas como textos.

Operações comuns:
```
dna = "ATGCGTAC"

print(len(dna))       # tamanho da string
print(dna[0])         # primeiro caractere (A)
print(dna[-1])        # último caractere (C)
print(dna.lower())    # minúsculas
print(dna.count("A")) # contar quantos 'A'
print(dna.replace("T", "U")) # DNA -> RNA
```
## 5. Exemplo de manipulação de String com dado Biológico: Contagem de Nucleotídeos em DNA

```
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

## 6. Exercício Prático

Tarefa:
Escreva um programa que:
- Peça ao usuário para digitar uma sequência de DNA.
- Calcule quantos A, T, G, C existem.
- Mostre a porcentagem de cada base na sequência.

---

## 7. Funções Úteis: Strings 

### Funções para Strings

As strings em Python possuem várias funções prontas que facilitam a análise de sequências de DNA, RNA e proteínas.

| Função | Descrição | Exemplo |
|--------|-----------|---------|
| `len(s)` | Retorna o tamanho da string | `len("ATGC") → 4` |
| `s.upper()` | Converte para maiúsculas | `"atgc".upper() → "ATGC"` |
| `s.lower()` | Converte para minúsculas | `"ATGC".lower() → "atgc"` |
| `s.count(x)` | Conta ocorrências de um caractere/substring | `"ATGCAT".count("A") → 2` |
| `s.find(x)` | Retorna o índice da primeira ocorrência | `"ATGC".find("G") → 2` |
| `s.replace(a,b)` | Substitui `a` por `b` | `"ATGC".replace("T","U") → "AUGC"` |
| `s[::-1]` | Inverte a string | `"ATGC"[::-1] → "CGTA"` |

**Exemplo prático com DNA**  
```
dna = "atgcgtta"

print("Sequência original:", dna)
print("Maiúsculas:", dna.upper())
print("Quantidade de A:", dna.count("a"))
print("Posição da primeira ocorrência de G:", dna.find("g"))
print("DNA para RNA:", dna.replace("t", "u"))
print("Sequência invertida:", dna[::-1])
```

## Agora veja o exemplo utilizando formatação de Strings na mensagem e cálculos também
```
# Exemplo: calcular a porcentagem de alunos aprovados em uma turma

# Número total de alunos
total_alunos = 40

# Número de alunos aprovados
alunos_aprovados = 28

# Cálculo da porcentagem
porcentagem_aprovados = (alunos_aprovados / total_alunos) * 100 #Se você quiser pode usar a função para arendondar e definir as casas decimais.

print(f"Total de alunos: {total_alunos}") #Note que temos uma formatação da mensagem aqui 
print(f"Alunos aprovados: {alunos_aprovados}")
print(f"Porcentagem de aprovados: {porcentagem_aprovados:.2f}%")
```

## Resumo do Módulo

- Algoritmo = conjunto de passos para resolver um problema.
- Variáveis armazenam dados, podem ser de tipos diferentes.
- Python usa operadores aritméticos, lógicos e relacionais.
- Entrada/saída é feita com input() e print().
- Strings são fundamentais em bioinformática (sequências).
- Exemplo aplicado: contagem de nucleotídeos em DNA.
