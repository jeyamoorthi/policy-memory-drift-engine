from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recommendation import generate_recommendations
from pathlib import Path
import json
import os

app = FastAPI(title="Policy Impact API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Resolve output file path relative to this script's location
SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = SCRIPT_DIR.parent / "output"


@app.get("/health")
def health_check():
    """Health check endpoint for connectivity testing."""
    return {"status": "ok"}


def read_latest():
    """Read the latest policy signal from the output file."""
    if not OUTPUT_FILE.exists():
        return None

    try:
        with open(OUTPUT_FILE, "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        if not lines:
            return None

        return json.loads(lines[-1])
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in output file: {e}")
    except Exception as e:
        raise RuntimeError(f"Error reading output file: {e}")


@app.get("/latest")
def get_latest_policy_analysis():
    """Get the latest policy analysis without recommendations."""
    try:
        data = read_latest()
        if not data:
            return {"status": "no data yet"}
        return data
    except Exception as e:
        return {"error": str(e)}


@app.get("/latest-with-recommendations")
def get_latest_with_recommendations():
    """Get the latest policy analysis with AI-generated recommendations."""
    try:
        data = read_latest()
        if not data:
            return {"status": "no data yet"}

        recommendations = generate_recommendations(
            signal=data["signal"],
            domain=data["domain"],
            impact=data["impact"],
            stakeholders=data["stakeholders"],
        )

        data["recommendations"] = recommendations
        return data
    except Exception as e:
        return {"error": str(e)}
