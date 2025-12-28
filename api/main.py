from fastapi import FastAPI
from pydantic import BaseModel
import json
import glob
import os

app = FastAPI()

OUTPUT_DIR = "./output/policy_results"


class PolicyRequest(BaseModel):
    signal: str


@app.post("/analyze")
def analyze_policy(req: PolicyRequest):
    # Send signal to Pathway
    os.system(
        f'curl -X POST http://localhost:8001 '
        f'-H "Content-Type: application/json" '
        f'-d \'{{"signal":"{req.signal}"}}\''
    )

    # Read latest Pathway output
    files = sorted(glob.glob(f"{OUTPUT_DIR}/*.json"))
    if not files:
        return {"status": "processing"}

    with open(files[-1]) as f:
        return json.load(f)

@app.get("/latest-with-recommendations")
def latest_with_recommendations():
    if latest_result is None:
        return {"status": "no data"}

    recs = generate_recommendations(
        signal=latest_result["signal"],
        domain=latest_result["domain"],
        impact=latest_result["impact"],
        stakeholders=latest_result["stakeholders"],
    )

    return {
        **latest_result,
        "recommendations": recs,
    }
