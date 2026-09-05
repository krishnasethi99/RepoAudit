def onboarding_risk_explainer(risk_result):
    explanations = []

    missing_dependencies = risk_result.get("missing_dependencies", [])
    missing_env_vars = risk_result.get("missing_env_vars", [])
    missing_sections = risk_result.get("missing_documentation_sections", [])
    likely_entrypoint = risk_result.get("likely_entrypoint")

    for dependency in missing_dependencies:
        explanations.append(f"Dependency '{dependency}' is imported by the project but not declared in requirements.txt or pyproject.toml.")

    for env_var in missing_env_vars:
        explanations.append(f"Environment variable '{env_var}' is required by the code but not documented in .env.example.")

    for section in missing_sections:
        explanations.append(f"README is missing the '{section}' section.")

    if likely_entrypoint:
        explanations.append(f"Detected application entrypoint: {likely_entrypoint}")
    else:
        explanations.append("No obvious application entrypoint was detected.")

    return explanations

def top_onboarding_risks(risk_result):            
    risks = []

    missing_dependencies = risk_result.get("missing_dependencies", [])
    missing_env_vars = risk_result.get("missing_env_vars", [])
    missing_sections = risk_result.get("missing_documentation_sections", [])
    likely_entrypoint = risk_result.get("likely_entrypoint")

# Heuristic onboarding-impact weights.
# These are not scientific scores and may be refined later.
    for dependency in missing_dependencies:
        risks.append({
            "severity": 30,
            "message": (
                f"Dependency '{dependency}' is imported "
                f"but not declared."
            )
        })

    for env_var in missing_env_vars:
        risks.append({
            "severity": 25,
            "message": (
                f"Environment variable '{env_var}' "
                f"is undocumented."
            )
        })

    for section in missing_sections:
        risks.append({
            "severity": 10,
            "message": (
                f"README missing '{section}' section."
            )
        })

    if not likely_entrypoint:
        risks.append({
            "severity": 15,
            "message": (
                "No application entrypoint detected."
            )
        })

    risks.sort(
        key=lambda risk: risk["severity"],
        reverse=True
    )

    return risks[:3]