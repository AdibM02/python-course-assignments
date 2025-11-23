"""Business logic for DNA to Protein translation.

This module handles DNA sequence validation and translation to protein sequences
using the standard genetic code table.
"""

import re
from typing import Optional

try:
    from Bio.Seq import Seq
    from Bio.Data.CodonTable import standard_dna_table
    BIOPYTHON_AVAILABLE = True
except ImportError:
    BIOPYTHON_AVAILABLE = False
    standard_dna_table = None


GENETIC_CODE_REGEX = re.compile(r'^[ATCGatcg]+$')


def validate_sequence(sequence: str) -> bool:
    """Validate that sequence contains only A, T, C, G (case-insensitive).

    Args:
        sequence: DNA sequence string

    Returns:
        True if sequence is valid, False otherwise
    """
    if not sequence:
        return False
    return bool(GENETIC_CODE_REGEX.fullmatch(sequence.strip()))


def translate_dna_to_protein(sequence: str) -> str:
    """Translate DNA sequence to protein using standard genetic code.

    Rules implemented:
    - Only A/T/C/G characters allowed (caller should validate first).
    - Find first ATG (start codon); if present start from it, otherwise start from beginning.
    - Translate in-frame codons (3 bases).
    - Stop at first stop codon (TAA, TAG, TGA).
    - Use one-letter amino acid codes.
    - Incomplete trailing codons are ignored.

    Args:
        sequence: DNA sequence (should be validated first)

    Returns:
        Protein sequence as one-letter amino acid codes
    """
    if not sequence:
        return ""

    dna = sequence.upper().strip()

    # Find start codon (ATG)
    start = dna.find('ATG')
    if start == -1:
        start = 0

    coding = dna[start:]

    # Use Biopython if available
    if BIOPYTHON_AVAILABLE:
        try:
            seq_obj = Seq(coding)
            protein = str(seq_obj.translate(to_stop=True))
            return protein
        except Exception:
            # Fall through to local implementation
            pass

    # Fallback: Use standard genetic code from Biopython if available
    if BIOPYTHON_AVAILABLE and standard_dna_table:
        try:
            protein = []
            for i in range(0, len(coding) - 2, 3):
                codon = coding[i:i+3]
                if len(codon) == 3:
                    aa = standard_dna_table.forward_table.get(codon, '*')
                    if aa == '*':
                        break
                    protein.append(aa)
            return ''.join(protein)
        except Exception:
            pass

    # Last resort: Local genetic code dictionary
    genetic_code = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    protein = []
    i = 0
    while i + 2 < len(coding):
        codon = coding[i:i+3]
        aa = genetic_code.get(codon, '')
        if aa == '*':
            break
        if aa:
            protein.append(aa)
        i += 3

    return ''.join(protein)
