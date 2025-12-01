# 🚀 Quick Start: Deploy to GitHub

## Your Situation
- ✅ You created a GitHub repository: `uniprotkb-protein-finder`
- ✅ You want to deploy the UniProtKB Protein Finder project to it
- ✅ You want it as a standalone repository (not part of the course folder)

## Quick Deployment (Choose One Method)

### ⚡ Method 1: PowerShell Script (EASIEST for Windows)

```powershell
# From the day04 directory, run:
.\deploy_to_github.ps1 "C:\Users\YourUsername\path\to\uniprotkb-protein-finder"
```

This will:
- ✅ Copy all necessary files
- ✅ Skip course-specific documentation
- ✅ Show you the next steps

### Method 2: Batch Commands (if script doesn't work)

From a PowerShell terminal in the day04 directory:

```powershell
# Create or navigate to your GitHub repository folder
$repoPath = "C:\path\to\uniprotkb-protein-finder"
New-Item -ItemType Directory -Path $repoPath -Force | Out-Null

# Copy essential files
Copy-Item main.py, ui.py, logic.py, config.py, requirements.txt, .env.example, LICENSE, README.md -Destination $repoPath -Force
Copy-Item .gitignore -Destination $repoPath -Force
Copy-Item .github -Destination $repoPath -Recurse -Force

# Navigate and push to GitHub
cd $repoPath
git init
git add .
git commit -m "Initial commit: UniProtKB Protein Finder"
git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git
git branch -M main
git push -u origin main
```

### Method 3: Manual Copy

1. Go to your `uniprotkb-protein-finder` folder on your computer
2. Copy these files from `day04/`:
   - `main.py`
   - `ui.py`
   - `logic.py`
   - `config.py`
   - `requirements.txt`
   - `.env.example`
   - `.gitignore`
   - `LICENSE`
   - `README.md`
3. Copy this folder: `.github/` (entire directory)

4. Then from PowerShell in that folder:
```powershell
git init
git add .
git commit -m "Initial commit: UniProtKB Protein Finder"
git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git
git branch -M main
git push -u origin main
```

---

## After Deployment

### Verify Files on GitHub

Visit: `https://github.com/yourusername/uniprotkb-protein-finder`

You should see:
- ✅ `main.py`, `ui.py`, `logic.py`, `config.py`
- ✅ `requirements.txt`, `.env.example`
- ✅ `.gitignore`, `LICENSE`, `README.md`
- ✅ `.github/` folder with `copilot-instructions.md`

You should NOT see:
- ❌ `DEPLOYMENT_GUIDE.md` (deployment helpers only)
- ❌ `deploy_to_github.py` or `deploy_to_github.ps1` (not needed)
- ❌ `CONVERSION_SUMMARY.md`, `SETUP_GUIDE.md` (course docs)
- ❌ `output/` or `__pycache__/` folders

### Test Your Deployed Repository

Clone it locally and test:

```powershell
# Clone your new repository
git clone https://github.com/yourusername/uniprotkb-protein-finder.git
cd uniprotkb-protein-finder

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

## Troubleshooting

### "git: command not found"
Install Git: https://git-scm.com/

### "fatal: not a git repository"
Run `git init` in your repository folder first

### "PowerShell script disabled"
Run this once in PowerShell as Administrator:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "Permission denied (publickey)"
Set up GitHub SSH key or use personal access token

### Can't find your files after pushing
Make sure you:
1. Used `git add .` (includes hidden files like `.github/`)
2. Ran `git commit -m "message"`
3. Ran `git push -u origin main`

---

## What Gets Deployed

### ✅ Standalone App Files
- `main.py` — Entry point
- `ui.py` — GUI
- `logic.py` — API & file I/O (with CSV logging)
- `config.py` — Configuration
- `requirements.txt` — Dependencies
- `.env.example` — Config template
- `.gitignore` — Git ignore rules
- `LICENSE` — MIT License
- `README.md` — Documentation
- `.github/copilot-instructions.md` — Dev guide

### ❌ NOT Deployed (Course Helpers)
- `DEPLOYMENT_GUIDE.md`
- `deploy_to_github.py`
- `deploy_to_github.ps1`
- `CONVERSION_SUMMARY.md`
- `SETUP_GUIDE.md`
- `COMPLETION_CHECKLIST.md`
- `output/` generated files
- `__pycache__/` cache

---

## Next: What You Can Do With Your GitHub Repo

1. **Share with others**: Copy the GitHub link and send it
2. **Contribute**: Add features, fix bugs, document
3. **Set up CI/CD**: Add GitHub Actions for automated testing
4. **Track versions**: Create releases with git tags
5. **Collaborate**: Invite others to contribute

---

## Need More Details?

Read the full deployment guide in your day04 folder:
`DEPLOYMENT_GUIDE.md`

It has:
- Detailed step-by-step instructions
- Multiple options for different systems
- Troubleshooting guide
- Verification checklist

---

**Ready? Start with Method 1 above! 🚀**
