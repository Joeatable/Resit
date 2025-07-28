# spliced_noncoding_genes.py
# Extract noncoding genes that contain valid splice donor/acceptor introns

import re

# Valid splice site combinations
valid_signals = {"GTAG", "GCAG", "ATAC"}

# Get user input
signal = input("Enter splice signal (GTAG / GCAG / ATAC): ").strip().upper()
if signal not in valid_signals:
    print("Error: only GTAG / GCAG / ATAC are allowed.")
    exit()

donor, acceptor = signal[:2], signal[2:]
pattern_str = f"(?=({donor}[ACGT]{{0,10000}}?{acceptor}))"
splice_pattern = re.compile(pattern_str)
# Regex to identify noncoding genes and extract gene name
gene_pattern = re.compile(r'gene:([^\s]+)')
is_protein_coding = re.compile(r'gene_biotype:protein_coding')

# Dictionary to hold matched genes
spliced_genes = {}

# Initialize
current_gene = None
current_seq = ""

# Read file
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current_gene and current_seq:
                introns = splice_pattern.findall(current_seq)
                if introns:
                    spliced_genes[current_gene] = (current_seq, len(introns))
            if not is_protein_coding.search(line):
                match = gene_pattern.search(line)
                current_gene = match.group(1) if match else None
                current_seq = ""
            else:
                current_gene = None
                current_seq = ""
        elif current_gene:
            current_seq += line

# Process final gene
if current_gene and current_seq:
    introns = splice_pattern.findall(current_seq)
    if introns:
        spliced_genes[current_gene] = (current_seq, len(introns))

# Write output
output_file = f"{signal}_spliced_genes.fa"
with open(output_file, "w") as out:
    for gene, (seq, count) in spliced_genes.items():
        out.write(f">{gene} | introns: {count}\n{seq}\n")

print(f"Finished! {len(spliced_genes)} genes with introns found and written to {output_file}.")
