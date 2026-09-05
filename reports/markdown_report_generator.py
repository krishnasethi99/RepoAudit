def generate_markdown_report(
    repo_info,
    risk_result,
    top_risks,
    explanations,
    output_file="repoaudit_report.md"
):

    lines = []

    lines.append("# REPOAUDIT v1.0")
    lines.append("")
    lines.append("# RepoAudit Report")
    lines.append("")

    lines.append("## Repository")
    lines.append(repo_info["repository_name"])
    lines.append("")

    lines.append("## Repository Summary")
    lines.append(f"- Python Files: {repo_info['total_python_files']}")
    lines.append(f"- Env Files: {repo_info['total_env_files']}")
    lines.append(f"- Markdown Files: {repo_info['total_markdown_files']}")
    lines.append(f"- Total Files: {repo_info['total_files']}")
    lines.append(f"- README: {'Yes' if repo_info['has_readme'] else 'No'}")
    lines.append(f"- Dockerfile: {'Yes' if repo_info['has_dockerfile'] else 'No'}")
    lines.append(
        f"- Requirements File: {'Yes' if repo_info['has_requirements'] else 'No'}"
    )
    lines.append("")

    lines.append("## Onboarding Score")
    lines.append(
        f"**{risk_result['onboarding_score']}/100 ({risk_result['risk_level']})**"
    )

    risk_count = risk_result["risk_count"]

    if risk_count:
        lines.append(f"Risk Count: {risk_count}")

    lines.append("")

    score_breakdown = risk_result.get("score_breakdown", [])

    penalties = [
        item for item in score_breakdown
        if item[1] < 0
    ]

    passed_checks = [
        item for item in score_breakdown
        if item[1] == 0
    ]

    lines.append("## Score Breakdown")

    if penalties:
        for reason, impact in penalties:
            lines.append(f"- {reason} ({impact})")
    else:
        lines.append("- No penalties")

    lines.append("")

    lines.append("## Checks Passed")

    if passed_checks:
        for reason, _ in passed_checks:
            lines.append(f"- {reason}")
    else:
        lines.append("- None")

    lines.append("")

    lines.append("## Missing Dependencies")

    missing_deps = risk_result.get("missing_dependencies", [])

    if missing_deps:
        for dep in missing_deps:
            lines.append(f"- {dep}")
    else:
        lines.append("- None")

    lines.append("")

    lines.append("## Missing Environment Variables")

    missing_env_vars = risk_result.get("missing_env_vars", [])

    if missing_env_vars:
        for env_var in missing_env_vars:
            lines.append(f"- {env_var}")
    else:
        lines.append("- None")

    lines.append("")

    lines.append("## Missing Documentation Sections")

    missing_sections = risk_result.get(
        "missing_documentation_sections",
        []
    )

    if missing_sections:
        for section in missing_sections:
            lines.append(f"- {section}")
    else:
        lines.append("- None")

    lines.append("")

    lines.append("## Likely Entrypoint")

    entrypoint = risk_result.get(
        "likely_entrypoint",
        "Not detected"
    )

    lines.append(entrypoint if entrypoint else "Not detected")

    lines.append("")

    lines.append("## Top Onboarding Risks")

    if top_risks:
        for i, risk in enumerate(top_risks, start=1):
            lines.append(f"{i}. {risk['message']}")
    else:
        lines.append("- None")

    lines.append("")

    lines.append("## Detailed Findings")

    if explanations:
        for explanation in explanations:
            lines.append(f"- {explanation}")
    else:
        lines.append("- No findings")

    lines.append("")
    lines.append("---")
    lines.append("Analysis Complete")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_file