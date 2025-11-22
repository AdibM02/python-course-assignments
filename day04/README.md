# UniProtKB Protein Finder - Day 04

A Tkinter GUI application that searches UniProtKB for proteins, retrieves their sequences and domain information, and exports the data as structured JSON.

###Prompts sent to VS code copilot (GPT-5 mini):
In the folder day04, create a Python project structured into at least two files:

ui.py — contains the GUI layer (Tkinter)

logic.py — contains the "business logic" and external API handling

Program Requirements

Purpose

Build a Tkinter GUI application that allows the user to enter:

A protein name (free text input field)

A species (dropdown list box of common species, with custom text entry option)

The program will search UniProtKB for the matching protein and species.

Search and Data Retrieval

Use the Biopython library where applicable (e.g., sequence parsing).

Query UniProtKB API to retrieve:

The full protein sequence

Its annotated regions/domains and their names

For each domain/region, extract and store:

Name/description

Amino acid sequence

The program should validate:

If the protein name or species is not found, ask the user again with a clear message instead of crashing.

Output Format

Save the retrieved data into a structured .json file.

Environment Variable Support

Load configuration using environment variables stored in a file ignored by Git (e.g., .env), including:

Contact email (required for API querying if needed)

Any optional configuration flags

Use standard environment variable loading approach (dotenv allowed).

GUI Requirements

Display:

One text input field for protein name

One dropdown list (plus manual override option) for species name

A search button

A status message area

After execution:

Inform the user if the search succeeded and where the JSON output was saved.

Technical Notes

Follow clean code best practices.

Use exception handling with clear user-facing error messages.

Ensure UI remains responsive (consider threading if needed).

## Features

- **GUI Search Interface**: Enter protein name and select species (with custom entry option)
- **UniProtKB Integration**: Queries the UniProtKB REST API for protein data
- **Domain Extraction**: Automatically extracts protein domains, regions, and active sites with sequences
- **JSON Export**: Saves results in structured JSON format with full sequence and domain details
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
3. **Click Search**: Queries UniProtKB and retrieves data
4. **View Results**: Status area shows success/error messages and output file path

### Example Searches

- **Protein**: "hemoglobin" | **Species**: "Human"
- **Protein**: "TP53" (tumor suppressor) | **Species**: "Human"
- **Protein**: "lactase" | **Species**: "Human"
- **Protein**: "lacZ" | **Species**: "E. coli"

## JSON Output Format

When a search succeeds, data is saved to `output/protein_<name>_<timestamp>.json`:

```json
{
  "protein_name": "HBA_HUMAN",
  "species": "Homo sapiens",
  "full_sequence": "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHG...",
  "sequence_length": 141,
  "domains": [
    {
      "name": "Globin",
      "type": "Domain",
      "start": 1,
      "end": 141,
      "sequence": "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHG..."
    }
  ],
  "exported_at": "2025-11-22T15:30:45.123456"
}
```

## File Descriptions

### `main.py`
Entry point that sets up the module path and launches the GUI.

### `ui.py`
Tkinter GUI layer:
- Text input for protein name
- Dropdown combobox for species selection
- Search button that triggers background thread
- Status display area with color coding
- Error message dialogs

**Threading**: Search runs on a separate thread to keep UI responsive.

### `logic.py`
Business logic and API handling:
- `UniProtKBClient`: Queries UniProtKB REST API
- `ProteinSearchService`: High-level search and export orchestration
- `ProteinDataExporter`: Converts data to JSON
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
