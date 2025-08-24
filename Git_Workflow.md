
# Git Workflow for AI Communication Surveillance App

This document explains the step-by-step process to manage the repository, push local changes, and handle remote conflicts.

---

## 1. Initialize Local Repository

```bash
cd path/to/Email_Surveilance_App
git init


Initializes an empty Git repository in your local folder.

2. Add Remote Origin
git remote add origin https://github.com/sathishbabu89/AI_Communication_Surveillance.git


Connects your local repository to the GitHub repository.

3. Check Status
git status


Shows untracked files and changes.

4. Add Files to Commit
git add app.py classify.py requirements.txt


Adds specific files to the staging area.

Do not add .env with API keys; instead use .env.example.

5. Commit Changes
git commit -m "Initial commit with Streamlit app, classify module, and sample CSV"


Creates a commit with a message describing the changes.

6. Rename Branch to Main
git branch -M main


Ensures your local branch is named main to match GitHub.

7. Push Changes to GitHub
Option 1: Safe Merge (Recommended)
git pull origin main --allow-unrelated-histories
# Resolve any merge conflicts if prompted
git add <resolved_file>
git commit -m "Resolve merge conflicts"
git push -u origin main


Pulls remote changes first to avoid conflicts.

Merge conflicts need to be resolved before pushing.

Option 2: Force Push (Use with Caution)
git push -u origin main --force


Overwrites remote repository with local changes.

Only use if you are sure the remote commits can be replaced.

8. Update Local Repository
git pull origin main


Fetches and merges remote changes regularly to stay up-to-date.

9. General Notes

Use .gitignore to exclude sensitive or unnecessary files:

.env
__pycache__/
*.pyc
my_env/


For environment variables, use .env or .env.example
