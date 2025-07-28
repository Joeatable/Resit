import re

def restriction_sites(dna, recognition_seq):
    # Check if sequences contain only ACGT
    if not re.fullmatch(r'[ACGT]+', dna) or not re.fullmatch(r'[ACGT]+', recognition_seq):
        return "Error: Invalid DNA or recognition sequence."
    
    # Find all matches and return 1-based positions
    positions = []
    for m in re.finditer(f"(?={recognition_seq})", dna):
        positions.append(m.start()+1)
    return positions
# Example usage
dna_seq = "AAGCTTGAATTCAAGCTT"
enzyme = "AAGCTT"
print(restriction_sites(dna_seq, enzyme))
# ➜ [1, 13]
