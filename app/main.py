import pathway as pw

from policy_ingest import SignalSchema
from policy_classifier import detect_policy_domain
from impact_agent import impact_score
from stakeholder_agent import resolve_stakeholders
from format_agent import format_output


def main():
    signals, _ = pw.io.http.rest_connector(
        host="0.0.0.0",
        port=8001,
        schema=SignalSchema,
    )

    enriched = signals.select(
        signal=pw.this.signal,
        domain=detect_policy_domain(pw.this.signal),
        impact=impact_score(pw.this.signal),
        stakeholders=resolve_stakeholders(
            detect_policy_domain(pw.this.signal)
        ),
    )

    final = enriched.select(
        output=format_output(
            pw.this.signal,
            pw.this.domain,
            pw.this.impact,
            pw.this.stakeholders,
        )
    )

    pw.debug.compute_and_print(final)
    pw.run()


if __name__ == "__main__":
    main()
