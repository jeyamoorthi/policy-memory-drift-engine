from fastapi import FastAPI
import random
import time
import threading

app = FastAPI()

signals = [
    {"signal": "inflation_up"},
    {"signal": "fuel_subsidy_increase"},
    {"signal": "food_price_spike"},
]

@app.get("/signal")
def get_signal():
    return random.choice(signals)

def run_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

if __name__ == "__main__":
    run_server()
