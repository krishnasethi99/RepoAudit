# RepoAudit

RepoAudit is a static repository onboarding auditor that helps developers identify what could prevent a new contributor from successfully cloning, configuring, and running a codebase.

Given a GitHub repository URL, RepoAudit clones the repository, analyzes its structure, dependencies, environment variables, documentation, and application entrypoints, then generates a comprehensive onboarding readiness report with a score, risks, and actionable findings.

The goal is simple:

> "If a new developer joined this project today, what would stop them from running it successfully?"

---

# Why RepoAudit?

One of the biggest challenges when joining an unfamiliar codebase is discovering hidden requirements:

- Missing dependencies
- Undocumented environment variables
- Incomplete setup instructions
- Missing README sections
- Unknown application entrypoints
- Configuration assumptions

Developers often spend hours figuring these out manually.

RepoAudit automates that discovery process and highlights onboarding risks immediately.

---

# Features

## Repository Analysis

- Scans repository structure
- Counts source files and project assets
- Detects README files
- Detects Dockerfiles
- Detects requirements files
- Detects pyproject.toml files
- Detects environment templates

---

## Python AST Analysis

Uses Python's Abstract Syntax Tree (AST) module to analyze source code safely without executing it.

Extracts:

- Imports
- Environment variable usage
- Function calls
- Project metadata

---

## Dependency Analysis

Detects:

- Imported packages
- Declared packages
- Missing dependencies
- Unused dependencies

Supports:

- requirements.txt
- pyproject.toml
- Poetry dependencies

---

## Environment Variable Analysis

Detects:

- Environment variables used in code
- Environment variables declared in .env.example
- Missing environment variables

Examples:

```python
os.getenv("OPENAI_API_KEY")
```

```python
os.environ["DATABASE_URL"]
```

---

## Documentation Analysis

Checks README quality and onboarding completeness.

Detects missing sections such as:

- Installation
- Usage
- Configuration
- Environment Variables
- Contributing

---

## Entrypoint Detection

Attempts to identify the primary application entrypoint.

Examples:

```text
main.py
app.py
server.py
run.py
```

Also analyzes:

```python
if __name__ == "__main__":
```

patterns.

---

## Onboarding Risk Scoring

Generates an onboarding score from:

```text
0 → 100
```

Higher score = easier onboarding.

Example:

```text
95/100 READY
```

---

## Risk Explanation Engine

Converts raw analysis findings into human-readable onboarding risks.

Example:

```text
Dependency 'flask' is imported but not declared.
```

instead of:

```text
missing_dependencies = ['flask']
```

---

## Report Generation

Produces:

### Console Report

Human-readable terminal output.

### Markdown Report

Automatically generates:

```text
repoaudit_report.md
```

for sharing or documentation.

---

# Example Output

```text
Repository:
example-server-python-flask

Onboarding Score: 95/100 (READY)

Checks Passed:
- README found
- Entrypoint detected
- Dependencies declared
- Environment variables documented

Missing Documentation Sections:
- contributing

Top Onboarding Risks:
1. README missing 'contributing' section.
```

---

# Architecture

```text
GitHub URL
      │
      ▼
GitHub Fetcher
      │
      ▼
Repository Scanner
      │
      ▼
Python AST Scanner
      │
      ▼
Analyzers
├── Dependency Analyzer
├── Environment Analyzer
├── Documentation Analyzer
└── Entrypoint Analyzer
      │
      ▼
Risk Scorer
      │
      ▼
Risk Explainer
      │
      ▼
Report Generators
├── Console Report
└── Markdown Report
```

---

# Project Structure

```text
RepoAudit/
│
├── analyzers/
│   ├── dependency_analyzer.py
│   ├── documentation_analyzer.py
│   ├── entrypoint_analyzer.py
│   ├── env_analyzer.py
│   └── risk_scorer.py
│
├── explainers/
│   └── onboarding_risk_explainer.py
│
├── fetchers/
│   └── github_fetcher.py
│
├── models/
│   └── final_report.py
│
├── reports/
│   ├── console_report_generator.py
│   └── markdown_report_generator.py
│
├── scanners/
│   ├── repository_scanner.py
│   └── python_ast_scanner.py
│
├── LICENSE
├── requirements.txt
├── README.md
└── main.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/krishnasethi99/RepoAudit.git
cd RepoAudit
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

- Python 3.14+
- Git installed and available in PATH

---

# Usage

Run:

```bash
python main.py
```

Enter a GitHub repository URL:

```text
Enter GitHub Repository URL:
https://github.com/user/repository
```

RepoAudit will:

1. Clone the repository
2. Analyze project structure
3. Analyze dependencies
4. Analyze environment variables
5. Analyze documentation
6. Detect application entrypoint
7. Generate onboarding score
8. Generate onboarding report

---

# Scoring System

RepoAudit starts every repository at:

```text
100 points
```

Points are deducted based on onboarding risks.

### Example Deductions

| Issue | Penalty |
|---------|---------|
| Missing README | -20 |
| Missing Dependency | -10 |
| Missing Environment Variables | -15 |
| Missing Documentation Section | -5 |
| Entrypoint Not Detected | -15 |

---

## Risk Levels

| Score | Level |
|---------|---------|
| 90 - 100 | READY |
| 70 - 89 | MINOR_FRICTION |
| 40 - 69 | DIFFICULT |
| Below 40 | HIGH_RISK |

---

# Example Findings

## Dependency Risk

```text
Dependency 'flask' is imported but not declared.
```

---

## Environment Variable Risk

```text
OPENAI_API_KEY is used but not documented.
```

---

## Documentation Risk

```text
README missing 'Installation' section.
```

---

## Entrypoint Risk

```text
No clear application entrypoint detected.
```

---

# Current Limitations

RepoAudit is intentionally designed as a static analysis tool.

Currently it:

✅ Analyzes source code

✅ Analyzes documentation

✅ Analyzes dependency declarations

✅ Analyzes environment configuration

❌ Does not execute code

❌ Does not run tests

❌ Does not verify runtime services

❌ Does not verify deployment configuration

---

# Future Scope

## Runtime Assumption Analyzer

Detect hidden runtime requirements:

- PostgreSQL
- MySQL
- Redis
- RabbitMQ
- Kafka
- External APIs

---

## Docker Analysis

Analyze:

- Dockerfiles
- Docker Compose
- Container startup commands
- Container dependencies

---

## CI/CD Analysis

Analyze:

- GitHub Actions
- GitLab CI
- Jenkins Pipelines
- Deployment workflows

---

## Configuration Drift Detection

Identify contradictions between:

- README
- requirements.txt
- pyproject.toml
- .env.example
- Source code

---

## Multi-Language Support

Planned support for:

- JavaScript
- TypeScript
- Java
- Go
- Rust
- C#

---

## Visual Reports

Generate:

- HTML Reports
- Dependency Graphs
- Risk Dashboards
- Onboarding Health Metrics

---

## Repository Comparison

Compare multiple repositories and rank them by onboarding readiness.

---

# Development Philosophy

RepoAudit was built around a simple principle:

> Understanding a repository should not require running it.

The tool focuses on extracting evidence directly from source code and project structure to help developers quickly assess onboarding complexity before spending hours debugging setup issues.

---

# Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

Feel free to open an issue or submit a pull request.

---

# Author

**Krishna Sethi**

GitHub:
https://github.com/krishnasethi99

---

# License

This project is licensed under the MIT License.

See the LICENSE file for details.