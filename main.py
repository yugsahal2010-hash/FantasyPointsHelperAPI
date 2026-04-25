from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/weighted-average")
def weighted_average_api(payload: dict):
    try:
        values = payload["values"]
        decay = 0.85
        n = len(values)
        weights = [decay ** (n - i - 1) for i in range(n)]
        total_weight = sum(weights)
        result = sum(v * w for v, w in zip(values, weights)) / total_weight
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
