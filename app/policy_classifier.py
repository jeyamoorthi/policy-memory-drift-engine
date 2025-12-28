import pathway as pw

@pw.udf
def detect_policy_domain(signal: str) -> str:
    s = signal.lower()
    if "inflation" in s or "interest" in s:
        return "finance"
    if "food" in s or "fertilizer" in s:
        return "agriculture"
    if "fuel" in s or "energy" in s:
        return "energy"
    return "general"
