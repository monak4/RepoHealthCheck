# RepoHealthCheck
This workflow automatically runs a health check on the repository, analyzing commit history and branch structure to identify potential issues such as inadequate code reviews or missing documentation.

# How to use

1. **Add the Workflow File**
   
   Save the workflow files in the src folder to the repository `.github/workflows/health_check.yml`.
   
2. **Add the Health Check Script**
   
   And then add the health_check.py file to the root of your repository.

3. **Commit and Push**
   
   Commit both files to your repository and push them to the `main` branch.

4. **Trigger the Workflow**
   
   The workflow will automatically run whenever:
   - A new commit is pushed to the `main` branch.
   - A pull request is created or updated.

# Features
## 1. Commit History Check
**Purpose**:

Ensures commit messages are meaningful and provide sufficient context.

**What it does**:

- Retrieves the commit log using git log.
- Checks if commit messages are too short (less than 10 characters).
- Reports any commits with inadequate messages.

**Example Issue Reported**:
```
Commit 3 has a short message: 'Fix'
```

## 2. Branch Structure Check
**Purpose**:

Helps maintain a clean and manageable branch structure.

**What it does**:

- Lists all remote branches using git branch -r.
- Counts the total number of remote branches.
- Reports if the number of branches exceeds a defined threshold (default: 10).

**Example Issue Reported**:
```
Too many remote branches. Consider cleaning up.
```

## 3. Documentation Check
**Purpose**:

Ensures that essential documentation files are present and up-to-date.

**What it does**:

- Checks for the presence of commonly used documentation files, such as:
  - README.md
  - CONTRIBUTING.md
  - docs/index.md
- Analyzes the last modification date of these files.
- Reports missing files or files that have not been updated for over 180 days (default threshold).

**Example Issues Reported**:
```
Documentation file 'README.md' is outdated (last updated 200 days ago).
Documentation file missing: CONTRIBUTING.md
```

# Output
The workflow will output any detected issues in the Actions logs. Look for the "Run health check" step to see detailed results.

# Customization
- **Commit Message Length**:
  
  Adjust the minimum length for valid commit messages by modifying the condition in `check_commit_history`.

- **Branch Threshold**:
  
  Change the threshold for the number of branches in `check_branch_structure`.

- **Documentation Files**:
  
  Add or remove file names in the `doc_files` list in `check_documentation`.

- **Update Threshold**:
  
  Modify the `180` days threshold in `check_documentation` to suit your requirements.

# How It Works
The script runs these checks sequentially and reports all detected issues. If no issues are found, it confirms that all checks have passed.

**Example Output (All Checks Passed)**:
```
Running health checks...
All checks passed!
```

**Example Output (With Issues)**:
```
Running health checks...
Issues found:
 - Commit 3 has a short message: 'Fix'
 - Too many remote branches. Consider cleaning up.
 - Documentation file 'README.md' is outdated (last updated 200 days ago).
 - Documentation file missing: CONTRIBUTING.md
```
