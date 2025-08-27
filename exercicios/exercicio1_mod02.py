## Você pode ter feito totalmente diferente, isto é apenas uma forma.

dna = input("Digite uma sequência de DNA: ").upper()
motivo = input("Digite o motivo a ser buscado: ").upper()

posicoes = []

for i in range(len(dna) - len(motivo) + 1):
    if dna[i:i+len(motivo)] == motivo:
        posicoes.append(i)

if posicoes:
    print("Motivo encontrado nas posições:", posicoes)
else:
    print("Motivo não encontrado na sequência.")

