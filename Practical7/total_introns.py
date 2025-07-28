# total_introns.py
# Identify all possible introns: each GT followed by a downstream AG

import re

# Input DNA sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Find all GT and AG positions
donor_sites = [m.start() for m in re.finditer(r'GT', seq)]
acceptor_sites = [m.start() for m in re.finditer(r'AG', seq)]

introns = []

# For each GT, find all downstream AG
for d in donor_sites:
    for a in acceptor_sites:
        if a > d + 1:  # Ensure AG comes after GT
            intron_seq = seq[d:a+2]  # include AG (a+2 because AG is 2bp)
            introns.append(intron_seq)

# Output
print("Total number of possible introns:", len(introns))
