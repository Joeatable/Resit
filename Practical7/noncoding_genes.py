import re  # Import regular expressions module

# Compile regex patterns to match gene name and biotype
gene_name = re.compile(r'gene:([^\s]+)')  
biotype = re.compile(r'gene_biotype:([^\s]+)')  

noncoding_genes = {}  # Dictionary to store non-coding genes and their sequences

# Open the FASTA file
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as data:
    current_gene = None  # Current gene name
    current_seq = ""     # Current sequence
    current_biotype = "" # Current gene's biotype

    # Read file line by line
    for line in data:
        line = line.strip()
        if line.startswith(">"):  # Header line encountered
            # Process previous gene if it's non-coding
            if current_gene and current_biotype != "protein_coding":
                noncoding_genes[current_gene] = current_seq
            
            # Extract gene name and biotype from header
            gene_match = gene_name.search(line)
            bio_match = biotype.search(line)
            current_gene = gene_match.group(1) if gene_match else None
            current_biotype = bio_match.group(1) if bio_match else ""
            current_seq = ""  # Reset sequence accumulator
        else:
            current_seq += line  # Accumulate sequence data

    # Process the last gene in the file
    if current_gene and current_biotype != "protein_coding":
        noncoding_genes[current_gene] = current_seq

# Write results to output file
with open("noncoding_genes.fa", "w") as out:
    for gene, seq in noncoding_genes.items():
        out.write(f">{gene}\n")
        # Format sequence with max 60 characters per line
        for i in range(0, len(seq), 60):
            out.write(seq[i:i+60] + "\n")

# Print completion message
print(f"Finished! A total of {len(noncoding_genes)} noncoding genes have been written to noncoding_genes.fa.")