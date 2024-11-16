import subprocess
import re

def check_commit_history():
    result = subprocess.run(['git', 'log', '--pretty=format:%s'], stdout=subprocess.PIPE, text=True)
    commits = result.stdout.split('\n')
    issues = []
    
    # commit message check (Exsample: short message)
    for i, commit in enumerate(commits):
        if len(commit) < 10:
            issues.append(f"Commit {i+1} has a short message: '{commit}'")
    return issues

def check_branch_structure():
    result = subprocess.run(['git', 'branch', '-r'], stdout=subprocess.PIPE, text=True)
    branches = result.stdout.split('\n')
    issues = []

    if len(branches) > 10:
        issues.append("Too many remote branches. Consider cleaning up.")
    return issues

def main():
    print("Running health checks...")
    issues = []
    issues.extend(check_commit_history())
    issues.extend(check_branch_structure())
    
    if not issues:
        print("All checks passed!")
    else:
        print("Issues found:")
        for issue in issues:
            print(f" - {issue}")

if __name__ == "__main__":
    main()
