def risk_scorer(dependency_result, env_result, doc_result, entrypoint_result):
    result = {
        "onboarding_score": 100,
        "risk_factors": [],
        "score_breakdown": [],
        "risk_level": "Unknown",
        "risk_counter": 0,
        "missing_dependencies": [],
        "missing_env_vars": [],
        "missing_documentation_sections": [],
        "likely_entrypoint": None
    }

    score = 100

    missing_dependencies = dependency_result.get("missing_dependencies", [])
    missing_env_vars = env_result.get("missing_env_vars", [])
    missing_sections = doc_result.get("missing_sections", [])
    has_readme = doc_result.get("has_readme", False)
    likely_entrypoint = entrypoint_result.get("likely_entrypoint")

    if not has_readme:
        score -= 20
        result["score_breakdown"].append(("README missing", -20))
        result["risk_factors"].append("README not found")

    if missing_dependencies:
        penalty = min(len(missing_dependencies) * 10, 30)
        score -= penalty
        count = len(missing_dependencies)
        label = (f"{count} missing dependency"
            if count == 1
            else f"{count} missing dependencies"
        )
        result["score_breakdown"].append((label, -penalty))
        result["risk_factors"].append(label)

    if missing_env_vars:
        penalty = min(len(missing_env_vars) * 5, 20)
        score -= penalty
        count = len(missing_env_vars)
        label = (f"{count} undocumented environment variable"
            if count == 1
            else f"{count} undocumented environment variables"
        )
        result["score_breakdown"].append((label, -penalty))
        result["risk_factors"].append(label)

    if not likely_entrypoint:
        score -= 10
        result["score_breakdown"].append(("No entrypoint detected", -10))
        result["risk_factors"].append("No entrypoint detected")

    if missing_sections:
        penalty = min(len(missing_sections) * 5, 15)
        score -= penalty
        count = len(missing_sections)
        label = (f"{count} missing documentation section"
            if count == 1
            else f"{count} missing documentation sections"
        )
        result["score_breakdown"].append((label, -penalty))
        result["risk_factors"].append(label)

    if has_readme:
        result["score_breakdown"].append(("README found", 0))

    if likely_entrypoint:
        result["score_breakdown"].append(("Entrypoint detected", 0))

    if not missing_dependencies:
        result["score_breakdown"].append(("Dependencies declared", 0))
    if not missing_env_vars:
        result["score_breakdown"].append(("Environment variables documented", 0))
    if not missing_sections:
        result["score_breakdown"].append(("Documentation sections present", 0))

    result["likely_entrypoint"] = likely_entrypoint
    result["missing_dependencies"] = sorted(missing_dependencies)
    result["missing_env_vars"] = sorted(missing_env_vars)
    result["missing_documentation_sections"] = sorted(missing_sections)

    score = max(score, 0)
    if score >= 90:
        risk_level = "READY"
    elif score >= 70:
        risk_level = "MINOR_FRICTION"
    elif score >= 40:
        risk_level = "DIFFICULT"
    else:
        risk_level = "HIGH_RISK"

    result["onboarding_score"] = score
    result["risk_level"] = risk_level
    result["risk_count"] = len(result["risk_factors"])

    return result