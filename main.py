from pathlib import Path

from fetchers.github_fetcher import clone_repository

from scanners.repository_scanner import scan_repository
from scanners.python_ast_scanner import python_ast_scanner

from analyzers.dependency_analyzer import dependency_analyzer
from analyzers.env_analyzer import env_analyzer
from analyzers.documentation_analyzer import doc_analyzer
from analyzers.entrypoint_analyzer import entrypoint_analyzer
from analyzers.risk_scorer import risk_scorer

from explainers.onboarding_risk_explainer import (
    onboarding_risk_explainer,
    top_onboarding_risks
)

from models.final_report import build_final_report

from reports.console_report_generator import (
    generate_console_report
)
from reports.markdown_report_generator import (
    generate_markdown_report
)


def main():
    url = input("Enter GitHub Repository URL: ").strip()
    if not url:
        print("Repository URL is required.")
        return

    repo_path = clone_repository(url)

    if not repo_path:
        print("Repository analysis aborted.")
        return
    print(f"\nRepository cloned to:\n{repo_path}")

    # -------------------------
    # Evidence Extraction
    # -------------------------
    repo_info = scan_repository(repo_path)
    ast_info = python_ast_scanner(repo_info["python_files"])

    # -------------------------
    # Analysis
    # -------------------------
    dependency_result = dependency_analyzer(repo_info, ast_info)
    env_result = env_analyzer(repo_info, ast_info)
    doc_result = doc_analyzer(repo_info)
    entrypoint_result = entrypoint_analyzer(ast_info)
    risk_result = risk_scorer(dependency_result, env_result, doc_result, entrypoint_result)

    # -------------------------
    # Explanations
    # -------------------------
    explanations = onboarding_risk_explainer(risk_result)
    top_risks = top_onboarding_risks(risk_result)

    # -------------------------
    # Final Report
    # -------------------------
    repo_name = Path(repo_info["repo_path"]).name
    final_report = build_final_report(repo_name, risk_result, top_risks, explanations)

    # -------------------------
    # Output
    # -------------------------
    generate_console_report(repo_info, risk_result, top_risks, explanations)
    report_file = generate_markdown_report(repo_info, risk_result, top_risks, explanations)
    print(f"\nMarkdown report saved to: {report_file}")

if __name__ == "__main__":
    main()