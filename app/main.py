import pathway as pw


class SignalSchema(pw.Schema):
    signal: str


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


@pw.udf
def impact_score(signal: str) -> int:
    scores = {
        "inflation_up": 8,
        "fuel_subsidy_increase": 5,
        "food_price_spike": 9,
    }
    return scores.get(signal, 3)

def main():
    signals, writer = pw.io.http.rest_connector(
        host="0.0.0.0",
        port=8001,
        schema=SignalSchema,
    )

    enriched = signals.select(
        signal=pw.this.signal,
        domain=detect_policy_domain(pw.this.signal),
        impact=impact_score(pw.this.signal),
    )

    response = enriched.select(
        result=
            pw.this.signal
            + " | domain="
            + pw.this.domain
            + " | impact="
            + pw.apply(str, pw.this.impact)
    )

    writer(response)
    pw.run()



if __name__ == "__main__":
    main()
