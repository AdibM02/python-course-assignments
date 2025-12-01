# GitHub Repository Deployment Guide

## Overview
This guide explains how to deploy the UniProtKB Protein Finder project to your new GitHub repository.

## Prerequisites

1. **GitHub Account** — You should have created the repository `uniprotkb-protein-finder`
2. **Git Installed** — https://git-scm.com/
3. **GitHub CLI (optional)** — For easier authentication

## Files Being Deployed

The following files will be copied to your GitHub repository:

### Core Application Files
- `main.py` — Application entry point
- `ui.py` — Tkinter GUI layer
- `logic.py` — Business logic and API client
- `config.py` — Configuration management

### Configuration & Documentation
- `requirements.txt` — Python dependencies
- `.env.example` — Example environment variables
- `.gitignore` — Git ignore rules
- `LICENSE` — MIT License
- `README.md` — Project documentation
- `.github/copilot-instructions.md` — AI agent guidance

### Files NOT Deployed (Course-Specific)
- `CONVERSION_SUMMARY.md` — Course project notes
- `SETUP_GUIDE.md` — Course setup guide
- `COMPLETION_CHECKLIST.md` — Course checklist
- `deploy_to_github.py` — This deployment script
- `deploy_to_github.ps1` — This deployment script
- `output/` — Generated files
- `__pycache__/` — Python cache

---

## Deployment Options

### Option 1: Using PowerShell (Windows) — RECOMMENDED

```powershell
# Navigate to day04 directory
cd "c:\Users\user\OneDrive - weizmann.ac.il\Desktop\Weizman drive\Weizmann\MSc 1st year semester A\Python course\python-course-assignments\day04"

# Run the deployment script
.\deploy_to_github.ps1 "path\to\uniprotkb-protein-finder"
```

**Example:**
```powershell
.\deploy_to_github.ps1 "$env:USERPROFILE\Documents\GitHub\uniprotkb-protein-finder"
```

### Option 2: Using Python

```bash
cd day04
python deploy_to_github.py /path/to/uniprotkb-protein-finder/
```

### Option 3: Manual Copy (Windows File Explorer)

1. **Create destination folder** for the repository
2. **Copy these files from day04:**
   - `main.py`
   - `ui.py`
   - `logic.py`
   - `config.py`
   - `requirements.txt`
   - `.env.example`
   - `.gitignore`
   - `LICENSE`
   - `README.md`

3. **Copy this folder from day04:**
   - `.github/` (entire directory)

---

## Steps to Deploy to GitHub

### Step 1: Run Deployment Script

Choose one of the options above. For Windows PowerShell (easiest):

```powershell
.\deploy_to_github.ps1 "C:\Users\YourUsername\Documents\GitHub\uniprotkb-protein-finder"
```

### Step 2: Navigate to Repository

```bash
cd path/to/uniprotkb-protein-finder
```

### Step 3: Initialize Git (If New Folder)

```bash
git init
```

### Step 4: Add All Files

```bash
git add .
```

### Step 5: Create Initial Commit

```bash
git commit -m "Initial commit: UniProtKB Protein Finder"
```

### Step 6: Add Remote Repository

Replace `yourusername` with your GitHub username:

```bash
git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git
```

### Step 7: Rename Branch to Main (If Needed)

```bash
git branch -M main
```

### Step 8: Push to GitHub

```bash
git push -u origin main
```

---

## Complete Command Sequence

Here's the complete sequence you can copy and paste:

### PowerShell (Windows):
```powershell
# From day04 directory
.\deploy_to_github.ps1 "C:\path\to\uniprotkb-protein-finder"

# Navigate to repository
cd "C:\path\to\uniprotkb-protein-finder"

# Initialize git and push
git init
git add .
git commit -m "Initial commit: UniProtKB Protein Finder"
git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git
git branch -M main
git push -u origin main
```

### Bash (macOS/Linux):
```bash
# From day04 directory
python deploy_to_github.py /path/to/uniprotkb-protein-finder

# Navigate to repository
cd /path/to/uniprotkb-protein-finder

# Initialize git and push
git init
git add .
git commit -m "Initial commit: UniProtKB Protein Finder"
git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git
git branch -M main
git push -u origin main
```

---

## Troubleshooting

### "git: command not found"
**Solution**: Install Git from https://git-scm.com/

### "fatal: not a git repository"
**Solution**: Run `git init` in the destination directory first

### "remote origin already exists"
**Solution**: Remove the existing remote first:
```bash
git remote remove origin
git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git
```

### "Permission denied (publickey)"
**Solution**: Set up SSH key with GitHub:
https://docs.github.com/en/authentication/connecting-to-github-with-ssh

Or use HTTPS with personal access token:
```bash
git remote set-url origin https://yourusername:GITHUB_TOKEN@github.com/yourusername/uniprotkb-protein-finder.git
```

### "Push rejected: updates were rejected"
**Solution**: Your GitHub repository might have initial files. You can:
1. Force push (careful!): `git push -u origin main --force`
2. Or pull first: `git pull origin main` then push again

---

## Verification

After pushing to GitHub, verify:

1. **Visit**: https://github.com/yourusername/uniprotkb-protein-finder
2. **Check files are present:**
   - ✅ `main.py`
   - ✅ `ui.py`
   - ✅ `logic.py`
   - ✅ `config.py`
   - ✅ `requirements.txt`
   - ✅ `.env.example`
   - ✅ `.gitignore`
   - ✅ `LICENSE`
   - ✅ `README.md`
   - ✅ `.github/copilot-instructions.md`

3. **Check that COURSE files are NOT present:**
   - ❌ No `CONVERSION_SUMMARY.md`
   - ❌ No `SETUP_GUIDE.md`
   - ❌ No `COMPLETION_CHECKLIST.md`
   - ❌ No `deploy_to_github.py`
   - ❌ No `deploy_to_github.ps1`
   - ❌ No `output/` directory

---

## Final Steps

Once deployed to GitHub:

### 1. Update README.md (Optional)
If you want to customize the README with your GitHub username or additional info:
- Edit directly on GitHub or locally
- Commit and push changes

### 2. Add GitHub Actions (Optional)
Create `.github/workflows/tests.yml` for automated testing:
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: python main.py --help
```

### 3. Add Repository Topics (Optional)
On GitHub repository settings, add tags like:
- `python`
- `gui`
- `tkinter`
- `api`
- `protein`
- `bioinformatics`

### 4. Add Repository Description (Optional)
In repository settings, add:
- **Description**: "Search UniProtKB for proteins with a modern Tkinter GUI"
- **Website**: (if you have a website)

---

## What's Included

### ✅ Included in Standalone Repo
- Fully functional application
- All dependencies documented
- Configuration management
- Error handling
- Threading for responsive UI
- API integration
- File I/O (JSON exports)
- File logging (CSV search history)
- Comprehensive documentation
- AI agent guidance for developers

### ❌ NOT Included in Standalone Repo
- Course-specific files
- Deployment scripts (for cleaner repo)
- Generated output files
- Python cache files

---

## Next Steps After Deployment

1. **Clone the repository locally** (if you want to work from there):
   ```bash
   git clone https://github.com/yourusername/uniprotkb-protein-finder.git
   ```

2. **Set up local development:**
   ```bash
   cd uniprotkb-protein-finder
   pip install -r requirements.txt
   python main.py
   ```

3. **Make updates and push:**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```

4. **Share repository** with others by sharing the GitHub URL

---

## Support

If you encounter issues:
1. Check the Troubleshooting section above
2. Review GitHub documentation: https://docs.github.com/
3. Check Git documentation: https://git-scm.com/doc

---

**Good luck with your standalone repository! 🚀**
