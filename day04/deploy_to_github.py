#!/usr/bin/env python3
"""
Script to prepare UniProtKB Protein Finder for standalone GitHub repository deployment.

This script copies the essential files from the course repository to a standalone
project directory, excluding course-specific documentation.

Usage:
    python deploy_to_github.py <destination_path>

Example:
    python deploy_to_github.py ../../../uniprotkb-protein-finder/

Requirements:
    - Python 3.7+
    - Destination directory must be empty or a git repository
"""

import os
import shutil
import sys
from pathlib import Path

# Files to include in standalone repository
FILES_TO_COPY = [
    'main.py',
    'ui.py',
    'logic.py',
    'config.py',
    'requirements.txt',
    '.env.example',
    '.gitignore',
    'LICENSE',
    'README.md',
]

# Directories to include
DIRS_TO_COPY = [
    '.github',
]

# Files/dirs to EXCLUDE (course-specific)
EXCLUDE = [
    '__pycache__',
    'output',
    '.pyc',
    'CONVERSION_SUMMARY.md',
    'SETUP_GUIDE.md',
    'COMPLETION_CHECKLIST.md',
]


def should_copy(name):
    """Check if file/dir should be copied."""
    for exclude in EXCLUDE:
        if exclude in name:
            return False
    return True


def copy_project(dest_path):
    """Copy project files to destination."""
    source_path = Path(__file__).parent
    dest_path = Path(dest_path)

    # Create destination if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)

    print(f"📋 Copying UniProtKB Protein Finder to: {dest_path}")
    print()

    # Copy files
    for file in FILES_TO_COPY:
        src = source_path / file
        dst = dest_path / file
        if src.exists():
            shutil.copy2(src, dst)
            print(f"✅ {file}")
        else:
            print(f"⚠️  {file} (not found)")

    # Copy directories
    for dir_name in DIRS_TO_COPY:
        src = source_path / dir_name
        dst = dest_path / dir_name
        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"✅ {dir_name}/")
        else:
            print(f"⚠️  {dir_name}/ (not found)")

    print()
    print("════════════════════════════════════════════════════")
    print("✅ Project copied successfully!")
    print("════════════════════════════════════════════════════")
    print()
    print("Next steps:")
    print("1. cd to the destination directory")
    print("2. Initialize git (if not already done):")
    print("     git init")
    print("3. Add all files:")
    print("     git add .")
    print("4. Create initial commit:")
    print("     git commit -m 'Initial commit: UniProtKB Protein Finder'")
    print("5. Add remote and push:")
    print("     git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git")
    print("     git branch -M main")
    print("     git push -u origin main")
    print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <destination_path>")
        print(f"Example: python {sys.argv[0]} /path/to/uniprotkb-protein-finder/")
        sys.exit(1)

    dest = sys.argv[1]
    try:
        copy_project(dest)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
