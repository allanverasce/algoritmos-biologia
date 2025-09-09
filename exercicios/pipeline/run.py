import pipeline

# Caminho para o arquivo FASTQ (single-end)
raw_fastq = "SRR12047106.fastq"

# Etapa 1: Avaliação de qualidade
pipeline.run_fastqc(raw_fastq)

# Etapa 2: Trimagem e filtro de qualidade
trimmed_fastq = "SRR12047106_trimmed.fastq"
pipeline.run_fastx_toolkit(raw_fastq, output_fastq=trimmed_fastq)

# Etapa 3: Montagem com SPAdes
pipeline.run_spades(trimmed_fastq, output_dir="assembly_results")

