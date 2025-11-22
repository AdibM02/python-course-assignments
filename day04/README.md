# UniProtKB Protein Finder - Day 04

A Tkinter GUI application that searches UniProtKB for proteins, retrieves their sequences and domain information, and displays results directly in the interface.

## Features

- **GUI Search Interface**: Enter protein name and select species (with custom entry option)
- **Instant Results Display**: View search results directly in the GUI without saving to disk
- **UniProtKB Integration**: Queries the UniProtKB REST API for protein data
- **Domain Display**: Shows protein domains, regions, and active sites with sequences
- **Error Handling**: Validates input and provides clear user-facing error messages
- **Threading**: Keeps UI responsive during API queries
- **Environment Configuration**: Uses .env file for contact email and output settings

## Project Structure

```
day04/
├── main.py                 # Entry point to launch the application
├── ui.py                   # Tkinter GUI layer
├── logic.py                # Business logic and UniProtKB API handling
├── config.py               # Configuration management (.env loader)
├── .env.example            # Example environment file
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation

### 1. Install Dependencies

```bash
pip install -r day04/requirements.txt
```

Or manually:
```bash
pip install requests
```

Optional (for enhanced functionality):
```bash
pip install python-dotenv
pip install biopython
```

### 2. Configure Environment (Optional)

Copy `.env.example` to `.env` and add your contact email:

```bash
cp day04/.env.example day04/.env
```

Edit `day04/.env`:
```env
CONTACT_EMAIL=your.email@example.com
OUTPUT_DIR=./output
```

**Why the contact email?**
UniProtKB API requests should include a contact email. This helps them monitor usage and reach out if issues arise.

## Usage

### Run the Application

```bash
python day04/main.py
```

Or directly:
```bash
python day04/ui.py
```

### Using the GUI

1. **Enter Protein Name**: Type the name of a protein (e.g., "hemoglobin", "insulin", "lysozyme")
2. **Select Species** (optional): 
   - Choose from dropdown (Human, Mouse, E. coli, etc.)
   - Or type a custom species name
3. **Click Search**: Queries UniProtKB and displays results instantly in the GUI
4. **View Results**: 
   - Full protein sequence displayed
   - All domains and regions listed with positions and sequences
   - Formatted output showing protein name, species, and domain information

### Example Searches

- **Protein**: "hemoglobin" | **Species**: "Human"
- **Protein**: "TP53" (tumor suppressor) | **Species**: "Human"
- **Protein**: "lactase" | **Species**: "Human"
- **Protein**: "lacZ" | **Species**: "E. coli"

## Results Display Format

Results are displayed directly in the GUI (no file downloads):

```
✓ FOUND: HBB_HUMAN
Species: Homo sapiens
Sequence Length: 146 amino acids

Full Sequence:
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHG...

============================================================
DOMAINS & REGIONS (7 found):
============================================================

[1] Globin
    Type: Domain
    Position: 1-146
    Sequence: MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHG...

[2] Heme iron coordination
    Type: Active site
    Position: 92-92
    Sequence: H
```

## File Descriptions

### `main.py`
Entry point that sets up the module path and launches the GUI.

### `ui.py`
Tkinter GUI layer:
- Text input for protein name
- Dropdown combobox for species selection
- Search button that triggers background thread
- Live results display showing protein sequence and domains
- Error message dialogs with color coding

**Threading**: Search runs on a separate thread to keep UI responsive.
**Display**: Results formatted and shown directly in the GUI (no file output).

### `logic.py`
Business logic and API handling:
- `UniProtKBClient`: Queries UniProtKB REST API
- `ProteinSearchService`: High-level search with optional export
  - `search()`: Returns data for GUI display
  - `search_and_export()`: Legacy method that also exports to JSON
- `ProteinDataExporter`: Converts data to JSON (optional feature)
- Custom exceptions for clear error handling
- `SPECIES_MAP`: Maps common names to scientific names

### `config.py`
Configuration management:
- Loads `.env` file (if python-dotenv is available)
- Provides contact email and output directory settings
- Auto-creates output directory

## API Integration

The application uses the **UniProtKB REST API** (free, no authentication required):
- Base search: `https://rest.uniprot.org/uniprotkb/search`
- Entry fetch: `https://rest.uniprot.org/uniprotkb/{id}`

**Note**: The API respects rate limits. For high-volume queries, consider implementing retry logic or caching.

## Error Handling

The application handles several error scenarios:

| Error | User Message | Action |
|-------|--------------|--------|
| Protein not found | Clear message with suggestion to check name | Stays open for retry |
| Species not found in results | Suggests trying different name/species | Stays open for retry |
| Network error | Shows API error with troubleshooting tip | Stays open for retry |
| Missing input | Error dialog requires input | No API call made |
| Unexpected error | Shows error details | Stays open for retry |

## Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"
Install: `pip install requests`

### "Connection timeout" or "Failed to connect"
- Check internet connection
- Verify UniProtKB API is accessible: `https://rest.uniprot.org`
- Try again after a delay

### GUI doesn't appear
- Ensure Tkinter is installed (usually comes with Python)
- On Linux: `sudo apt-get install python3-tk`
- Try running: `python -c "import tkinter; print('OK')"`

### Output directory issues
- Check `OUTPUT_DIR` in `.env`
- Ensure the directory path is writable
- Default: `./output` in the day04 folder

## Code Architecture

### Separation of Concerns
- **ui.py**: Only handles GUI rendering and user interaction
- **logic.py**: Only handles API communication and data processing
- **config.py**: Centralized configuration
- **main.py**: Application entry point

### Key Design Patterns
- **Threading**: UI remains responsive during API calls
- **Exception Hierarchy**: Custom exceptions for clear error handling
- **Service Layer**: `ProteinSearchService` orchestrates high-level workflows
- **Graceful Degradation**: Optional dependencies (dotenv, Biopython) don't break core functionality

## Future Enhancements

- [ ] Add sequence alignment visualization
- [ ] Support batch queries from CSV
- [ ] Cache results locally to avoid redundant API calls
- [ ] Export to FASTA format
- [ ] Add protein structure visualization (PDB integration)
- [ ] Implement search history
- [ ] Add protein interaction network display

## References

- [UniProtKB REST API Documentation](https://www.uniprot.org/help/api)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Biopython](https://biopython.org/)

## Author Notes

This application demonstrates:
- Clean code practices with separation of concerns
- Responsive GUI with threading
- Error handling and validation
- Configuration management
- RESTful API integration
- JSON data export

Suitable for learning modern Python application architecture.
