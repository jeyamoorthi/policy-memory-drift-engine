import pathway as pw

@pw.udf
def impact_score(signal: str) -> int:
    scores = {
        "inflation_up": 8,
        "fuel_subsidy_increase": 5,
        "food_price_spike": 9,
    }
    return scores.get(signal, 3)
