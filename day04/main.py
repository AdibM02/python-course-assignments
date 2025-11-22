"""Entry point for UniProtKB Protein Finder application.

Run this script to launch the GUI.
"""

import sys
from pathlib import Path

# Ensure the day04 module is in the path
day04_path = Path(__file__).parent
sys.path.insert(0, str(day04_path))

from ui import run_gui


def main():
    """Main entry point."""
    try:
        run_gui()
    except Exception as e:
        print(f'Error launching application: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
