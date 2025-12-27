import time
import random
import pathway as pw


class NewsStream(pw.io.python.ConnectorSubject):
    def run(self):
        events = [
            {"signal": "inflation_up"},
            {"signal": "fuel_subsidy_increase"},
            {"signal": "food_price_spike"},
        ]

        # 🔥 CRITICAL: yield immediately at least once
        yield random.choice(events)

        while True:
            time.sleep(5)
            yield random.choice(events)
