#!/bin/bash

# GitHub Repository Initialization Script
# This script helps you initialize and push your portfolio to GitHub

echo "📚 GitHub Repository Setup Script"
echo "=================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Error: git is not installed."
    echo "Please install git from: https://git-scm.com/downloads"
    exit 1
fi

echo "✅ Git found"
echo ""

# Check if already a git repository
if [ -d ".git" ]; then
    echo "⚠️  This directory is already a git repository."
    read -p "Do you want to continue? This may overwrite existing remote. (y/n): " confirm
    if [ "$confirm" != "y" ]; then
        echo "Exiting..."
        exit 0
    fi
else
    echo "Initializing git repository..."
    git init
    echo "✅ Repository initialized"
fi

echo ""
read -p "Enter your GitHub username: " GITHUB_USER
read -p "Enter the repository name (e.g., portfolio): " REPO_NAME

echo ""
echo "Setting up .gitignore if not exists..."
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
.venv/
ENV/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local

# Build
build/
dist/
*.egg-info/

# Logs
*.log

# Testing
.pytest_cache/
.coverage
htmlcov/
EOF
    echo "✅ .gitignore created"
else
    echo "✅ .gitignore already exists"
fi

echo ""
echo "Adding all files to git..."
git add .

echo ""
echo "Creating initial commit..."
git commit -m "Initial commit: Portfolio website with Flask and modern UI" || echo "⚠️  No changes to commit or commit already exists"

echo ""
echo "Setting up remote repository..."
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

echo ""
echo "✅ Remote repository configured: https://github.com/${GITHUB_USER}/${REPO_NAME}"
echo ""
echo "📝 Next steps:"
echo "1. Create a new repository on GitHub: https://github.com/new"
echo "   - Repository name: ${REPO_NAME}"
echo "   - Make it public or private"
echo "   - DO NOT initialize with README, .gitignore, or license"
echo ""
echo "2. After creating the repository on GitHub, run:"
echo "   git push -u origin main"
echo ""
echo "3. Your portfolio will be pushed to GitHub!"
echo ""

read -p "Do you want to push now? (y/n): " push_now
if [ "$push_now" = "y" ]; then
    echo ""
    echo "Pushing to GitHub..."
    git push -u origin main

    if [ $? -eq 0 ]; then
        echo ""
        echo "🎉 Success! Your portfolio is now on GitHub!"
        echo "View it at: https://github.com/${GITHUB_USER}/${REPO_NAME}"
    else
        echo ""
        echo "❌ Push failed. Please make sure:"
        echo "1. You created the repository on GitHub"
        echo "2. You have the correct permissions"
        echo "3. You're authenticated with GitHub"
        echo ""
        echo "Try running: git push -u origin main"
    fi
else
    echo ""
    echo "Remember to push your code when ready:"
    echo "git push -u origin main"
fi

echo ""
echo "✨ All done!"

