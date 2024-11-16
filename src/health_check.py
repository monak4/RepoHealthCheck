import os
import subprocess
import time
import sys

def check_commit_history():
    result = subprocess.run(['git', 'log', '--pretty=format:%s'], stdout=subprocess.PIPE, text=True)
    commits = result.stdout.split('\n')
    issues = []
    
    for i, commit in enumerate(commits):
        if len(commit) < 10:  # Too short commit msg
            issues.append(f"Commit {i+1} has a short message: '{commit}'")
    return issues

def check_branch_structure():
    result = subprocess.run(['git', 'branch', '-r'], stdout=subprocess.PIPE, text=True)
    branches = result.stdout.split('\n')
    issues = []
    
    if len(branches) > 10:
        issues.append("Too many remote branches. Consider cleaning up.")
    return issues

def check_documentation():
    doc_files = ['README.md']  # Common Document Files
    issues = []

    for file in doc_files:
        if not os.path.exists(file):
            issues.append(f"Documentation file missing: {file}")
        else:
            last_modified = os.path.getmtime(file)
            days_since_update = (time.time() - last_modified) / (60 * 60 * 24)
            if days_since_update > 180:  # Not updated for more than 180 days
                issues.append(f"Documentation file '{file}' is outdated (last updated {int(days_since_update)} days ago).")
    return issues

def main():
    print("Running health checks...")
    issues = []
    issues.extend(check_commit_history())
    issues.extend(check_branch_structure())
    issues.extend(check_documentation())
    
    if not issues:
        print("All checks passed!")
    else:
        for issue in issues:
            print(f"::warning file=health_check.py::{issue}")
        sys.exit(1)

if __name__ == "__main__":
    main()
