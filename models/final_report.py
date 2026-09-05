def build_final_report(repo_name, risk_result, top_risks, explanations):
    return {
        "repo_name": repo_name,
        "onboarding_score": risk_result["onboarding_score"],
        "missing_dependencies": risk_result["missing_dependencies"],
        "missing_env_vars": risk_result["missing_env_vars"],
        "missing_documentation_sections":
            risk_result["missing_documentation_sections"],
        "likely_entrypoint":
            risk_result["likely_entrypoint"],
        "top_risks": top_risks,
        "detailed_findings": explanations
    }