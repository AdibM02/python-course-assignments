# PowerShell script to deploy UniProtKB Protein Finder to GitHub repository
# 
# Usage (from day04 directory):
#   .\deploy_to_github.ps1 "C:\path\to\uniprotkb-protein-finder"
#
# Example:
#   .\deploy_to_github.ps1 "$env:USERPROFILE\Documents\uniprotkb-protein-finder"

param(
    [Parameter(Mandatory=$true, HelpMessage="Path to destination GitHub repository")]
    [string]$DestinationPath
)

# Files to copy
$filesToCopy = @(
    "main.py",
    "ui.py",
    "logic.py",
    "config.py",
    "requirements.txt",
    ".env.example",
    ".gitignore",
    "LICENSE",
    "README.md"
)

# Directories to copy
$dirsToCopy = @(
    ".github"
)

# Base path
$sourcePath = Get-Location

# Resolve destination path
$destPath = Resolve-Path $DestinationPath -ErrorAction SilentlyContinue
if (-not $destPath) {
    $destPath = $DestinationPath
}

Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "📋 Deploying UniProtKB Protein Finder" -ForegroundColor Green
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "Source: $sourcePath"
Write-Host "Destination: $destPath"
Write-Host ""

# Create destination if needed
if (-not (Test-Path $destPath)) {
    New-Item -ItemType Directory -Path $destPath -Force | Out-Null
    Write-Host "✅ Created destination directory"
}

# Copy files
Write-Host ""
Write-Host "Copying files..." -ForegroundColor Yellow
foreach ($file in $filesToCopy) {
    $src = Join-Path $sourcePath $file
    $dst = Join-Path $destPath $file
    
    if (Test-Path $src) {
        Copy-Item -Path $src -Destination $dst -Force
        Write-Host "  ✅ $file"
    } else {
        Write-Host "  ⚠️  $file (not found)" -ForegroundColor Yellow
    }
}

# Copy directories
Write-Host ""
Write-Host "Copying directories..." -ForegroundColor Yellow
foreach ($dir in $dirsToCopy) {
    $src = Join-Path $sourcePath $dir
    $dst = Join-Path $destPath $dir
    
    if (Test-Path $src) {
        if (Test-Path $dst) {
            Remove-Item -Path $dst -Recurse -Force
        }
        Copy-Item -Path $src -Destination $dst -Recurse -Force
        Write-Host "  ✅ $dir/"
    } else {
        Write-Host "  ⚠️  $dir/ (not found)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "✅ Deployment complete!" -ForegroundColor Green
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Navigate to the repository:"
Write-Host "   cd '$destPath'"
Write-Host ""
Write-Host "2. Initialize git (if not already done):"
Write-Host "   git init"
Write-Host ""
Write-Host "3. Add all files:"
Write-Host "   git add ."
Write-Host ""
Write-Host "4. Create initial commit:"
Write-Host "   git commit -m 'Initial commit: UniProtKB Protein Finder'"
Write-Host ""
Write-Host "5. Add remote and push:"
Write-Host "   git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git"
Write-Host "   git branch -M main"
Write-Host "   git push -u origin main"
Write-Host ""
