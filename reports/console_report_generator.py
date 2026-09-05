def generate_console_report(repo_info, risk_result, top_risks, explanations):

    print("REPOAUDIT v1.0")

    print("=" * 40)
    print("REPOAUDIT REPORT")
    print("=" * 40)
    
    print("\nRepository:")
    print(repo_info["repository_name"])

    print("\nRepository Summary:")
    print(f"Python Files: {repo_info['total_python_files']}")
    print(f"Env Files: {repo_info['total_env_files']}")
    print(f"Markdown Files: {repo_info['total_markdown_files']}")
    print(f"Total Files: {repo_info['total_files']}")
    print(f"README: {'Yes' if repo_info['has_readme'] else 'No'}")
    print(f"Dockerfile: {'Yes' if repo_info['has_dockerfile'] else 'No'}")
    print(f"Requirements File: {'Yes' if repo_info['has_requirements'] else 'No'}")

    print(f"\nOnboarding Score: {risk_result['onboarding_score']}/100 ({risk_result['risk_level']})")
    risk_count = risk_result["risk_count"]
    if risk_count:
        print(f"Risk Count: {risk_count}")

    score_breakdown = risk_result.get("score_breakdown", [])

    penalties = [
        item for item in score_breakdown
        if item[1] < 0
    ]

    passed_checks = [
        item for item in score_breakdown
        if item[1] == 0
    ]

    print("\nScore Breakdown:")

    if penalties:
        for reason, impact in penalties:
            print(f"- {reason} ({impact})")
    else:
        print("- No penalties")

    print("\nChecks Passed:")

    if passed_checks:
        for reason, _ in passed_checks:
            print(f"- {reason}")
    else:
        print("- None")

    print("\nMissing Dependencies:")
    missing_deps = risk_result.get("missing_dependencies", [])
    if missing_deps:
        for dep in missing_deps:
            print(f"- {dep}")
    else:
        print("- None")

    print("\nMissing Environment Variables:")
    missing_env_vars = risk_result.get("missing_env_vars", [])
    if missing_env_vars:
        for env_var in missing_env_vars:
            print(f"- {env_var}")
    else:
        print("- None")

    print("\nMissing Documentation Sections:")
    missing_sections = risk_result.get("missing_documentation_sections", [])
    if missing_sections:
        for section in missing_sections:
            print(f"- {section}")
    else:
        print("- None")

    print("\nLikely Entrypoint:")
    entrypoint = risk_result.get("likely_entrypoint", "Not detected")
    if entrypoint:
        print(entrypoint)
    else:
        print("Not detected")

    print("\nTop Onboarding Risks:")
    if top_risks:
        for i, risk in enumerate(top_risks, start=1):
            print(f"{i}. {risk['message']}")
    else:
        print("- None")

    print("\nDetailed Findings:")
    if explanations:
        for explanation in explanations:
            print(f"- {explanation}")
    else:
        print("No findings.")

    print("\n" + "=" * 40)
    print("Analysis Complete")
    print("=" * 40)
