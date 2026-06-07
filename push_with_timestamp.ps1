# Git Push Script with Timestamp
# Automatically commits and pushes all files with current date and time

$currentDateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMessage = "Update: $currentDateTime"

$projectPath = "C:\Users\mryad\Documents\workspace\databroIQ"

# Change to project directory
Set-Location $projectPath
Write-Host "=========================================="
Write-Host "Git Push with Timestamp"
Write-Host "=========================================="
Write-Host "Working Directory: $(Get-Location)"
Write-Host "Timestamp: $currentDateTime"
Write-Host ""

# Stage 1: Add all files
Write-Host "Stage 1: Adding all files..."
git add .
if ($LASTEXITCODE -eq 0) {
    Write-Host "Success: All files staged"
} else {
    Write-Host "Error: Failed to stage files"
    exit 1
}

# Check if there are changes
Write-Host ""
Write-Host "Checking for changes..."
$status = git status --porcelain
if (-not $status) {
    Write-Host "No changes to commit"
    exit 0
}

# Stage 2: Commit with timestamp
Write-Host ""
Write-Host "Stage 2: Committing with message: $commitMessage"
git commit -m "$commitMessage"
if ($LASTEXITCODE -eq 0) {
    Write-Host "Success: Commit created"
} else {
    Write-Host "Error: Commit failed"
    exit 1
}

# Stage 3: Push to remote
Write-Host ""
Write-Host "Stage 3: Pushing to GitHub..."
git push -u origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "Success: Push completed"
} else {
    Write-Host "Push status: Check messages above"
}

# Show recent commits
Write-Host ""
Write-Host "Recent commits:"
git log --oneline -5

Write-Host ""
Write-Host "=========================================="
Write-Host "Operation completed successfully!"
Write-Host "=========================================="
