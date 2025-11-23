#!/usr/bin/env python3
"""Entry point for DNA to Protein Translator application.

Run this script to launch the GUI.
"""

import sys
from pathlib import Path

# Ensure day03 module is in path
day03_path = Path(__file__).parent
sys.path.insert(0, str(day03_path))

from ui import main


if __name__ == '__main__':
    main()
