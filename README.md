# RepoAudit

RepoAudit is a Python-based repository onboarding analyzer that helps identify what might prevent a new developer from successfully running a project.

Instead of focusing on code quality, RepoAudit focuses on onboarding readiness by analyzing:

- Project dependencies
- Environment variables
- Documentation completeness
- Application entrypoints
- Configuration files

The tool generates an onboarding score, highlights onboarding risks, and produces both console and markdown reports.

---

# Problem

Many repositories are difficult to set up because of:

- Missing dependencies
- Undocumented environment variables
- Incomplete README files
- Hidden runtime assumptions
- Unclear application entrypoints

RepoAudit automatically scans a repository and identifies these issues before a developer spends time debugging setup problems.

---

# Features

## Repository Scanner

Detects:

- README files
- Dockerfiles
- requirements.txt
- pyproject.toml
- .env.example files

---

## Python AST Scanner

Parses Python source code using the Abstract Syntax Tree (AST).

Extracts:

- Imports
- Environment variable usage

---

## Dependency Analyzer

Compares:

- Imported packages
- Declared packages

Supports:

- requirements.txt
- pyproject.toml

Detects:

- Missing dependencies
- Unused dependencies

---

## Environment Analyzer

Identifies:

- Environment variables used by the application
- Environment variables documented in .env.example files

Detects:

- Missing environment variable documentation

---

## Documentation Analyzer

Analyzes README files for common onboarding sections:

- Installation
- Usage
- Configuration
- Contributing

Detects missing documentation sections.

---

## Entrypoint Analyzer

Attempts to identify the application's startup file.

Examples:

- main.py
- app.py
- run.py

---

## Risk Scoring Engine

Generates:

- Onboarding Score (0–100)
- Risk Level
- Risk Breakdown

Example:

```text
95/100 READY
70/100 MINOR_FRICTION
50/100 DIFFICULT
20/100 HIGH_RISK
```

---

# Project Structure

```text
RepoAudit/
│
├── analyzers/
│   ├── dependency_analyzer.py
│   ├── documentation_analyzer.py
│   ├── env_analyzer.py
│   ├── entrypoint_analyzer.py
│   └── risk_scorer.py
│
├── explainers/
│   └── onboarding_risk_explainer.py
│
├── fetchers/
│   └── github_fetcher.py
│
├── reports/
│   ├── console_report_generator.py
│   └── markdown_report_generator.py
│
├── scanners/
│   ├── repository_scanner.py
│   └── python_ast_scanner.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/RepoAudit.git
cd RepoAudit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run:

```bash
python main.py
```

Enter a GitHub repository URL:

```text
Enter GitHub Repository URL:
https://github.com/example/project
```

RepoAudit will:

1. Clone the repository
2. Analyze onboarding readiness
3. Generate reports

---

# Example Output

```text
Onboarding Score: 95/100 (READY)

Checks Passed:
- README found
- Dependencies declared
- Environment variables documented

Missing Documentation Sections:
- contributing

Likely Entrypoint:
app/main.py
```

---

# Generated Reports

RepoAudit generates:

### Console Report

Displayed directly in the terminal.

### Markdown Report

```text
repoaudit_report.md
```

Contains:

- Onboarding score
- Missing dependencies
- Missing environment variables
- Documentation issues
- Entrypoint detection
- Risk explanations

---

# Current Limitations

RepoAudit performs static analysis only.

It does not:

- Execute repository code
- Detect runtime failures
- Verify external services
- Validate deployment environments

---

# Future Scope

Potential future enhancements:

- Runtime assumption analysis
- Docker Compose analysis
- CI/CD pipeline analysis
- GitHub Actions analysis
- Database dependency detection
- API dependency detection
- Multi-language repository support
- Interactive HTML reports

---

# License

This project is licensed under the MIT License.

See the LICENSE file for details.