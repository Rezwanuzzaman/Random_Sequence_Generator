#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def generate_random_sequence(length=1000):
    """Generate a random DNA sequence of given length."""
    return ''.join(random.choice('ATGC') for _ in range(length))

def save_to_fasta(sequences, filename):
    """Save list of sequences to FASTA format."""
    with open(filename, 'w') as f:
        for i, seq in enumerate(sequences, 1):
            f.write(f">seq{i}\n{seq}\n")

def main():
    num_sequences = 10
    sequence_length = 1000
    sequences = [generate_random_sequence(sequence_length) for _ in range(num_sequences)]
    save_to_fasta(sequences, 'synthetic_sequences.fasta')
    print(f"{num_sequences} synthetic sequences saved to 'synthetic_sequences.fasta'.")

if __name__ == "__main__":
    main()

