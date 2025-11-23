# Day 03: DNA to Protein Translator (Refactored)

A clean, well-architected DNA-to-protein translation application with separated business logic, Biopython integration, and comprehensive tests.

## Overview

This project demonstrates **clean code principles** with:
- ✓ Separation of concerns (logic vs UI)
- ✓ Business logic independent of GUI
- ✓ External library integration (Biopython)
- ✓ Comprehensive unit tests
- ✓ Graceful fallback mechanisms

### Project Structure

```
day03/
├── logic.py           # Pure business logic (DNA validation, translation)
├── ui.py             # Tkinter GUI only (imports from logic.py)
├── main.py           # Application entry point
├── test_main.py      # Pytest test suite
├── requirements.txt  # Dependencies
└── README.md         # This file
```

## Architecture

### Clean Separation

**logic.py** - Business Logic (no UI code)
- `validate_sequence(sequence: str) -> bool` — Validates DNA sequence
- `translate_dna_to_protein(sequence: str) -> str` — Translates to amino acids
- Uses Biopython's standard genetic code table
- Falls back to local dictionary if Biopython unavailable

**ui.py** - User Interface (no translation code)
- `DNATranslatorGUI` class with Tkinter
- Imports functions from `logic.py`
- Error dialogs for invalid input
- Result display in read-only text area

**test_main.py** - Tests
- Imports directly from `logic.py`
- Tests independent of GUI
- 4 comprehensive test cases (all passing)

### Translation Rules

- **Start codon**: Find first `ATG`; if found, start there; otherwise start from position 0
- **Stop codons**: Stop at first `TAA`, `TAG`, or `TGA`
- **Validation**: Only A, T, C, G allowed (case-insensitive)
- **Output**: One-letter amino acid codes; incomplete codons ignored

## Installation

### Step 1: Python 3.7+

```bash
python --version
```

### Step 2: Install Dependencies

#### Option A: Individual packages

```bash
pip install biopython
pip install pytest
```

#### Option B: All at once

```bash
pip install biopython pytest
```

#### Option C: From requirements file

```bash
pip install -r requirements.txt
```

### What Each Package Does

| Package | Purpose | Required? | Notes |
|---------|---------|-----------|-------|
| **biopython** | Standard genetic code table | Optional | Falls back to built-in dict if unavailable |
| **pytest** | Test framework | Required for tests | Only needed to run test suite |

## Usage

### Run the GUI

```bash
python main.py
```

**Features:**
- Text input for DNA sequence (A, T, C, G only)
- "Translate" button to convert to protein
- Output displayed in read-only text area
- Error dialogs for invalid input

### Run Tests

```bash
pytest test_main.py -v
```

**Expected Results:**
```
test_translation_starts_at_first_atg PASSED
test_translation_stops_at_stop_codon PASSED
test_no_start_translate_from_beginning_and_ignore_incomplete PASSED
test_lowercase_input PASSED

====== 4 passed ======
```

### Use Programmatically

```python
from logic import translate_dna_to_protein, validate_sequence

if validate_sequence('ATGGCCATTGTAA'):
    protein = translate_dna_to_protein('ATGGCCATTGTAA')
    print(protein)  # Output: MAI
```

## File Descriptions

### logic.py
**Business logic layer** with no UI dependencies:

```python
def validate_sequence(sequence: str) -> bool:
    """Validate sequence contains only A, T, C, G."""

def translate_dna_to_protein(sequence: str) -> str:
    """Translate DNA to protein using standard genetic code."""
```

Features:
- Uses Biopython's `standard_dna_table` when available
- Falls back to hardcoded genetic code if needed
- Tries three methods in order:
  1. Biopython `Seq.translate(to_stop=True)`
  2. Biopython `standard_dna_table.forward_table`
  3. Built-in genetic code dictionary

### ui.py
**User interface layer** that uses logic:

```python
class DNATranslatorGUI:
    def _on_translate(self):
        # Get input
        seq = self.input_text.get('1.0', 'end').strip()
        
        # Validate using logic.py
        if not validate_sequence(seq):
            messagebox.showerror(...)
            return
        
        # Translate using logic.py
        protein = translate_dna_to_protein(seq)
        
        # Display result
        self.output_text.insert('1.0', protein)
```

Features:
- Clean Tkinter interface
- All logic imported from `logic.py`
- No hardcoded genetic code
- Error handling for user input

### test_main.py
**Test suite** for business logic:

```python
from logic import translate_dna_to_protein

def test_translation_starts_at_first_atg():
    assert translate_dna_to_protein('AAAATGAAACCC') == 'MKP'

def test_translation_stops_at_stop_codon():
    assert translate_dna_to_protein('ATGAAATAGGGT') == 'MK'
```

Features:
- Simple, straightforward tests
- No GUI interaction
- Easy to understand and extend
- Can be run independently

### main.py
**Application entry point**:

```python
from ui import main

if __name__ == '__main__':
    main()
```

## Key Improvements

### Before (Monolithic)
- All code in single file
- GUI mixed with business logic
- Hardcoded genetic code dictionary
- Difficult to test and maintain

### After (Refactored)
- Business logic separated to `logic.py`
- UI isolated in `ui.py`
- Biopython genetic code integration
- Simple, focused test suite
- Easy to understand, extend, and test

### Genetic Code Handling

**Old approach** (still used as fallback):
```python
genetic_code = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    # ... 60+ more entries manually typed
}
```

**New approach** (primary method):
```python
from Bio.Data.CodonTable import standard_dna_table

# Uses official NCBI genetic code table
aa = standard_dna_table.forward_table.get(codon, '*')
```

**Benefits:**
- Official standard from NCBI
- Maintained by Biopython project
- Less code in our project
- Reliable and tested

## Testing

### Running Tests

```bash
# From day03 directory
pytest test_main.py -v

# Or from project root
pytest day03/test_main.py -v
```

### Test Coverage

1. **ATG start codon detection**
   - Translates from first ATG if present
   - Starts from beginning if no ATG

2. **Stop codon handling**
   - Stops at TAA, TAG, or TGA
   - Doesn't include stop codon in output

3. **Incomplete codon handling**
   - Ignores trailing incomplete codons

4. **Case insensitivity**
   - Accepts lowercase and uppercase
   - Normalizes to uppercase internally

## Troubleshooting

### "No module named 'Bio'"
Biopython is optional. Install if you want official genetic code table:
```bash
pip install biopython
```

### "No module named 'pytest'"
Pytest is only needed for tests:
```bash
pip install pytest
```

### GUI doesn't launch
Ensure Tkinter is installed:
- Windows/macOS: Usually included with Python
- Linux: `sudo apt-get install python3-tk`

### Tests produce warnings
Biopython may warn about incomplete codons. This is normal; tests pass.

## Code Quality

- ✓ Type hints for clarity
- ✓ Docstrings for all functions
- ✓ Clean separation of concerns
- ✓ DRY principle (no code duplication)
- ✓ Error handling with user-friendly messages
- ✓ Comprehensive test coverage

## External Libraries

| Library | Purpose | Version | Link |
|---------|---------|---------|------|
| biopython | Standard genetic code table | >=1.81 | https://biopython.org |
| pytest | Testing framework | >=7.0.0 | https://pytest.org |

Both are optional; the app works without them using fallback implementations.

## Example Usage

### Via GUI
1. Run: `python main.py`
2. Enter: `ATGGCCATTGTAA`
3. Click: **Translate**
4. See: `MAI`

### Programmatically
```python
from logic import translate_dna_to_protein

result = translate_dna_to_protein('ATGGCCATTGTAA')
print(result)  # Output: MAI
```

### In Tests
```python
from logic import translate_dna_to_protein

def test_example():
    assert translate_dna_to_protein('ATG') == 'M'
```

## Next Steps

To further improve this project:

- [ ] Add support for alternative genetic codes
- [ ] Implement batch translation from FASTA files
- [ ] Add codon usage statistics
- [ ] Create CLI interface in addition to GUI
- [ ] Add protein property visualization
- [ ] Implement sequence alignment
- [ ] Export results to FASTA format

## Related Files

- `dna_to_protein_gui.py` — Old monolithic version (kept for reference)
- `DNA_complement.py` — Complementary DNA calculator (in day02)
- `test_main.py` — Test suite (comprehensive coverage)
