dna = input("Digite uma sequência de DNA: ").upper()

total = len(dna)

count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

print("Composição da sequência:")
print("A: ", count_A, "(", round(count_A/total*100, 2), "% )")
print("T: ", count_T, "(", round(count_T/total*100, 2), "% )")
print("G: ", count_G, "(", round(count_G/total*100, 2), "% )")
print("C: ", count_C, "(", round(count_C/total*100, 2), "% )")

