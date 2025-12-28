import pathway as pw

@pw.udf
def resolve_stakeholders(domain: str) -> str:
    if domain == "finance":
        return "consumers, banks, MSMEs, investors"
    if domain == "agriculture":
        return "farmers, agri-companies, consumers"
    if domain == "energy":
        return "households, transport, industries"
    return "general public"
