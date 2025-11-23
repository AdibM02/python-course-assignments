"""Tests for DNA to Protein translation logic."""

from logic import translate_dna_to_protein, validate_sequence


def test_translation_starts_at_first_atg():
    """Test that translation starts at first ATG codon."""
    assert translate_dna_to_protein('AAAATGAAACCC') == 'MKP'


def test_translation_stops_at_stop_codon():
    """Test that translation stops at first stop codon (TAA, TAG, TGA)."""
    assert translate_dna_to_protein('ATGAAATAGGGT') == 'MK'


def test_no_start_translate_from_beginning_and_ignore_incomplete():
    """Test translation from beginning if no ATG, and incomplete codons ignored."""
    assert translate_dna_to_protein('TTTGGGCC') == 'FG'


def test_lowercase_input():
    """Test that lowercase input is handled correctly."""
    assert translate_dna_to_protein('atgaaaTGG') == 'MKW'

