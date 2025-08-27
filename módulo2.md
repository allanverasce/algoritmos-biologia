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


