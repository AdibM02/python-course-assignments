# Day 03: DNA to Protein Translator

This directory contains an improved DNA-to-protein translation application with a modern GUI and comprehensive test suite.
## Prompts sent to VS code copilot (GPT-5 mini):
Test program:
Using pytest, lets try to build a test for the dna to protein program to validate that it works properly. 

Utilizing external library in day02 program: 
Lets try to build the dna to protein gui program again using 3rd-party library (dependencies) if there are such libraries that may make the code better - after implementing, list me the external libraries that you used



## Overview

### Modules

- **`dna_to_protein_gui.py`**
  - Main application with GUI and translation logic
  - Exports `translate_sequence_from_text(sequence: str) -> str` for use in tests and CLI scripts
  - Provides `DNATranslatorGUI` class for launching the interactive GUI
  - Uses **ttkbootstrap** (optional) for modern UI theming; falls back to tkinter if not available
  - Uses **Biopython** (optional) for robust translation; falls back to local codon table if not available

- **`test_main.py`**
  - Pytest-based test suite validating translation logic
  - Tests cover: ATG start codon detection, stop codon handling, case-insensitivity, invalid input rejection

### Translation Rules

- **Start codon**: Search for first `ATG` in the sequence; if found, start translation there; otherwise start from position 0
- **Stop codons**: Stop translation at first occurrence of `TAA`, `TAG`, or `TGA`
- **Input validation**: Only A, T, C, G allowed (case-insensitive)
- **Output**: One-letter amino acid codes; incomplete trailing codons ignored

## Installation

### Step 1: Install Python 3.7+

Ensure Python 3.7 or later is installed. Check your version:

```bash
python --version
```

### Step 2: Install Required Dependencies

Install the three main dependencies:

#### Option A: Install individually (pip)

```bash
pip install ttkbootstrap
pip install biopython
pip install pytest
```

#### Option B: Install all at once

```bash
pip install ttkbootstrap biopython pytest
```

#### Option C: Using a requirements.txt file (if present)

```bash
pip install -r requirements.txt
```

### What Each Package Does

| Package | Purpose | Required? | Notes |
|---------|---------|-----------|-------|
| **ttkbootstrap** | Modern GUI theming for Tkinter | Optional | GUI falls back to plain tkinter if not installed |
| **biopython** | Robust biological sequence translation | Optional | Falls back to built-in codon table if not installed |
| **pytest** | Unit testing framework | Required for tests | Only needed to run the test suite |

## Usage

### Run the GUI Application

Launch the interactive DNA-to-protein translator:

```bash
python -m day03.dna_to_protein_gui
```

Or from the day03 directory:

```bash
python dna_to_protein_gui.py
```

**GUI Features:**
- Enter a DNA sequence (A, T, C, G only)
- Click "Translate" to convert to amino acids
- Invalid sequences show error dialogs
- Output displayed in read-only text area

### Run the Test Suite

Execute all tests with pytest:

```bash
pytest test_main.py -v
```

Or from the day03 directory:

```bash
pytest test_main.py
```

**Expected Output:**
```
test_main.py::test_start_at_atg PASSED
test_main.py::test_stop_at_stop_codon PASSED
test_main.py::test_no_start_codon PASSED
test_main.py::test_case_insensitive PASSED

====== 4 passed in 0.XX s ======
```

### Use Translation Programmatically

Import and use the translation helper in your own scripts:

```python
from day03.dna_to_protein_gui import translate_sequence_from_text, validate_sequence

# Validate a sequence
if validate_sequence('ATGGCCATTGTAA'):
    # Translate it
    protein = translate_sequence_from_text('ATGGCCATTGTAA')
    print(protein)  # Output: MAI
```

## Project Structure

```
day03/
├── dna_to_protein_gui.py       # Main GUI and translation logic
├── test_main.py                 # Pytest test suite
├── README.md                    # This file
├── pyproject.toml              # Optional: Python project metadata
├── .python-version             # Optional: Python version specification
└── uv.lock                      # Optional: Dependency lock file (if using uv)
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'ttkbootstrap'"

**Solution:** ttkbootstrap is optional. The application will work with plain tkinter. To use modern themes:
```bash
pip install ttkbootstrap
```

### "ModuleNotFoundError: No module named 'Bio'"

**Solution:** Biopython is optional. The application uses a built-in codon table as fallback. To use Biopython:
```bash
pip install biopython
```

### "ModuleNotFoundError: No module named 'pytest'"

**Solution:** Pytest is only needed to run tests. Install it:
```bash
pip install pytest
```

### GUI Window Doesn't Appear

- Ensure tkinter is available (usually comes with Python on Windows/macOS)
- On Linux, you may need: `sudo apt-get install python3-tk`
- Try running the module directly:
  ```bash
  python dna_to_protein_gui.py
  ```

### Tests Fail to Import Module

Ensure you run pytest from the repository root, not from inside day03:
```bash
# Correct: run from repository root
pytest day03/test_main.py

# Or from day03 directory:
cd day03
pytest test_main.py
```

## Example Workflows

### Example 1: GUI Translation

1. Run the GUI:
   ```bash
   python dna_to_protein_gui.py
   ```
2. Enter: `ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG`
3. Click "Translate"
4. Result: `MAIVMGR*`

### Example 2: Command-Line Testing

```bash
pytest test_main.py -v --tb=short
```

### Example 3: Programmatic Use in Another Script

```python
from day03.dna_to_protein_gui import translate_sequence_from_text

# Batch translate multiple sequences
sequences = [
    'ATGTTTAAA',      # Start codon + 2 codons
    'GGGAAATAG',      # No start codon, stop at TAG
    'ATGGCC',         # Incomplete trailing codon
]

for seq in sequences:
    result = translate_sequence_from_text(seq)
    print(f"{seq:20} → {result}")
```

## Additional Notes

- **Performance**: Biopython translation is faster for large sequences; built-in fallback is suitable for learning/small sequences
- **Testing Strategy**: Tests import the translation function safely without instantiating the GUI, avoiding side effects
- **Validation**: All user input is validated before translation to reject invalid DNA sequences early
- **Compatibility**: The GUI gracefully degrades if optional libraries are missing; all functionality remains available with fallback implementations

## Questions or Issues?

Refer to the test cases in `test_main.py` for examples of expected behavior, or check inline documentation in `dna_to_protein_gui.py`.
