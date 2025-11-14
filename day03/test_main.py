from pathlib import Path
import importlib.util

# Load module from day02 without running it as __main__
MODULE_PATH = Path(__file__).resolve().parents[1] / 'day02' / 'dna_to_protein_gui.py'
spec = importlib.util.spec_from_file_location('dna_gui', str(MODULE_PATH))
dna_gui = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dna_gui)

GENETIC_CODE = {
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


def translate_using_class_method(seq: str) -> str:
    obj = object.__new__(dna_gui.DNATranslator)
    obj.genetic_code = GENETIC_CODE
    return dna_gui.DNATranslator.translate_dna_to_protein(obj, seq)


def test_translation_starts_at_first_atg():
    assert translate_using_class_method('AAAATGAAACCC') == 'MKP'


def test_translation_stops_at_stop_codon():
    assert translate_using_class_method('ATGAAATAGGGT') == 'MK'


def test_no_start_translate_from_beginning_and_ignore_incomplete():
    assert translate_using_class_method('TTTGGGCC') == 'FG'


def test_lowercase_input():
    assert translate_using_class_method('atgaaaTGG') == 'MKW'
