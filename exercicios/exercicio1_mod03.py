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
