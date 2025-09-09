import subprocess
import os

def run_fastqc(input_fastq, output_dir="fastqc_results"):
    """
    Função para Avaliação de qualidade com FastQC
    """
    os.makedirs(output_dir, exist_ok=True)
    cmd = ["fastqc", input_fastq, "-o", output_dir]
    print(f"Executando: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def run_fastx_toolkit(input_fastq, output_fastq="trimmed.fastq", quality_threshold=20, min_length=50):
    """
    Fazendo a Trimagem e filtro de qualidade com FASTX-Toolkit (fastq_quality_trimmer)
    """
    cmd = [
        "fastq_quality_trimmer",
        "-t", str(quality_threshold),  # limiar de qualidade
        "-l", str(min_length),         # comprimento mínimo
        "-i", input_fastq,
        "-o", output_fastq
    ]
    print(f"Executando: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def run_spades(input_fastq, output_dir="spades_output"):
    """
    Montagem com SPAdes (single-end)
    """
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        "spades.py",
        "-s", input_fastq,
        "-o", output_dir,
        "--only-assembler"
    ]
    print(f"Executando: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
