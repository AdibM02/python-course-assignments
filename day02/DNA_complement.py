#!/usr/bin/env python3
import sys

def get_dna_complement(sequence):
    """Return the complement of a DNA sequence"""
    DNA_complement = ""
    for base in sequence:
        if base == "A":
            DNA_complement += "T"
        elif base == "G":
            DNA_complement += "C"
        elif base == "T":
            DNA_complement += "A"
        elif base == "C":
            DNA_complement += "G"
    return DNA_complement

def main():
    # Check if a sequence was provided
    if len(sys.argv) != 2:
        print("Usage: python DNA_complement.py <DNA_sequence>")
        print("Example: python DNA_complement.py ATGCTA")
        sys.exit(1)
    
    # Get DNA sequence from command line argument
    DNA_original = sys.argv[1]
    
    # Get and print the complement
    DNA_complement = get_dna_complement(DNA_original)
    print(f"Original sequence: {DNA_original}")
    print(f"Complement sequence: {DNA_complement}")

if __name__ == "__main__":
    main()
