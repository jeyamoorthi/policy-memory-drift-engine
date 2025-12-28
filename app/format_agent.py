import pathway as pw

@pw.udf
def format_output(signal: str, domain: str, impact: int, stakeholders: str) -> str:
    return f"{signal} | domain={domain} | impact={impact} | stakeholders={stakeholders}"
