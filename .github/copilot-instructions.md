# AI Coding Agent Instructions

## Project Overview
Python course assignments repository containing progressively complex projects focused on DNA/protein bioinformatics applications and clean code architecture.

**Structure**: Each `dayXX/` folder is an independent project (day01–day04).

---

## Architecture & Major Components

### Day01–Day02: Foundational Scripts
- **day01**: Basic Python (`hello.py`)
- **day02**: Standalone utilities
  - `DNA_complement.py` — Command-line tool (CLI via `sys.argv`)
  - `triangle_area.py` — Input validation & math
  - `dna_to_protein_gui.py` — First attempt (monolithic, see day03 for refactored version)

### Day03: Clean Architecture Reference
**File structure** (separation of concerns):
```
day03/
├── logic.py          # Pure business logic (no UI, fully testable)
├── ui.py             # Tkinter GUI only (imports from logic)
├── main.py           # Entry point
├── test_main.py      # Pytest suite
```

**Key pattern**:
- `logic.py` exports `translate_dna_to_protein(seq)` and `validate_sequence(seq)`
- `ui.py` imports these functions; no translation code in UI
- `test_main.py` imports and tests `logic.py` directly

**Translation rules** (DNA → Protein):
1. Find first `ATG`; if found, start there; else start at position 0
2. Translate codons (3 bases) using standard genetic code
3. Stop at first `TAA`, `TAG`, or `TGA` stop codon
4. Return one-letter amino acid codes (no stop codon in output)
5. Ignore incomplete trailing codons

**Dependency strategy**:
- Try Biopython's `Seq.translate(to_stop=True)` (most reliable)
- Fallback to Biopython's `standard_dna_table.forward_table` (official NCBI table)
- Last resort: built-in genetic code dictionary (always available)

### Day04: API Integration & Threading
**File structure**:
```
day04/
├── main.py          # Entry point; ensures day04 in sys.path
├── ui.py            # Tkinter GUI with threading
├── logic.py         # UniProtKB API client + business logic
├── config.py        # Config loader (.env support)
```

**Key components**:
- `UniProtKBClient` — Queries UniProtKB REST API (queries `/search` then `/entry/{id}`)
- `ProteinSearchService` — High-level orchestration (search + extract data)
- `ProteinDataExporter` — JSON export (optional feature)
- `ProteinFinderGUI` — Tkinter UI with background thread for API calls

**Threading pattern** (day04/ui.py):
```python
def _on_search_clicked(self):
    thread = threading.Thread(target=self._search_worker, daemon=True)
    thread.start()

def _search_worker(self, protein_name, species):
    self.is_searching = True
    try:
        data = self.service.search(...)
    finally:
        self.is_searching = False
```
Prevents UI freeze during API queries; updates use `self.root.after()` for thread-safe GUI updates.

**API design**:
- Base search: `https://rest.uniprot.org/uniprotkb/search?query=...&format=json`
- Entry fetch: `https://rest.uniprot.org/uniprotkb/{id}?format=json`
- No authentication required; respects rate limits
- User-Agent header required (from `config.contact_email`)

**Species filtering**:
- `SPECIES_MAP` maps common names to scientific names (Human→Homo sapiens, etc.)
- Search returns top 10 results; UI filters by species or uses first match
- Falls back gracefully if species not found

---

## Development Workflow

### Testing (day03)
```bash
# Run tests
pytest day03/test_main.py -v

# Expected: 4 passing (start codon, stop codon, no start handling, case insensitivity)
```
Tests import directly from `logic.py`; no GUI testing needed.

### Running Applications
```bash
python day03/main.py   # DNA translator GUI
python day04/main.py   # UniProtKB protein finder GUI
```

### Configuration (day04)
- `.env` file optional; uses defaults if missing
- `CONTACT_EMAIL` — Required by UniProtKB API (user@example.com default)
- `OUTPUT_DIR` — JSON export location (./output default)
- See `config.py` for how dotenv is loaded with fallback

---

## Project-Specific Patterns

### 1. Separation of Concerns
- **Logic layer** (`logic.py`): No imports from tkinter; pure functions
- **UI layer** (`ui.py`): GUI only; business logic imported, not reimplemented
- **Config layer** (`config.py`): Centralized settings; optional external dependencies

### 2. Graceful Degradation
Example: Biopython genetic code (day03/logic.py)
```python
try:
    from Bio.Seq import Seq
except ImportError:
    Seq = None

# Later, try Biopython first, fall back to dict
if Seq is not None:
    protein = str(Seq(coding).translate(to_stop=True))
else:
    protein = translate_with_dict(coding)  # Using genetic_code dict
```
Core functionality works without optional dependencies.

### 3. GUI Threading Pattern
Always run long operations (API calls, file I/O) on background threads; update GUI via `root.after()` for thread safety.

### 4. Entry Points
Each day04 imports `sys.path` adjustment in `main.py`:
```python
day04_path = Path(__file__).parent
sys.path.insert(0, str(day04_path))
```
Ensures imports work when running from project root or subfolder.

### 5. Error Handling with Custom Exceptions
day04 defines project-specific exceptions for clarity:
```python
class ProteinNotFoundError(Exception): pass
class SpeciesNotFoundError(Exception): pass
class APIError(Exception): pass
```
Caught separately in UI for user-friendly error dialogs.

---

## Common Tasks

### Adding a New Feature to day04
1. Implement logic in `logic.py` (import UniProtKBClient, test independently)
2. Wire UI in `ui.py` (call logic functions, update UI with results)
3. If needs config: Add to `config.py`
4. Manual testing: `python day04/main.py`

### Running day03 Tests After Changes
```bash
cd day03 && pytest test_main.py -v
```
All 4 tests must pass; if translation logic changes, update tests.

### Debugging API Issues (day04)
1. Check `.env` contains valid `CONTACT_EMAIL`
2. Verify internet connection (API timeout = 10s)
3. Print response JSON: `print(json.dumps(data, indent=2))`
4. Check UniProtKB API status: https://rest.uniprot.org/

---

## Dependencies

| Day | Module | Required | Optional |
|-----|--------|----------|----------|
| 03  | tkinter | Yes | No* |
| 03  | biopython | No | Standard genetic code table |
| 03  | pytest | No | Tests only |
| 04  | tkinter | Yes | No* |
| 04  | requests | Yes | REST API queries |
| 04  | dotenv | No | .env file support |

*Tkinter included with Python distribution (except Linux: `apt-get install python3-tk`)

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `day03/logic.py` | DNA translation core; study for clean business logic |
| `day03/ui.py` | Tkinter UI template; no translation code here |
| `day04/logic.py` | UniProtKB API integration; study for REST client pattern |
| `day04/ui.py` | Threading pattern for responsive GUI |
| `day04/config.py` | Environment config with graceful degradation |

---

## Code Quality Standards

1. **Type hints** — Use for function signatures (e.g., `def foo(x: str) -> int:`)
2. **Docstrings** — Module and function level; describe rules and edge cases
3. **No hardcoded paths** — Use `Path(__file__).parent` or config
4. **Error messages** — User-friendly in dialogs; technical details in exceptions
5. **Imports** — Group by standard library, third-party, local; at top of file

---

## Contact & References

- **Project**: Weizmann MSc Python Course
- **UniProtKB API**: https://www.uniprot.org/help/api
- **Biopython**: https://biopython.org/
- **Tkinter**: https://docs.python.org/3/library/tkinter.html
