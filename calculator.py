from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CalculatorRequest(BaseModel):
    a: float
    b: float
    operation: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator", "operations": ["add", "subtract", "multiply", "divide"]}

@app.post("/calculate")
def calculate(request: CalculatorRequest):
    a, b, op = request.a, request.b, request.operation.lower()
    
    if op == "add":
        return {"result": a + b}
    elif op == "subtract":
        return {"result": a - b}
    elif op == "multiply":
        return {"result": a * b}
    elif op == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        return {"result": a / b}
    else:
        raise HTTPException(status_code=400, detail=f"Unknown operation: {op}. Use 'add', 'subtract', 'multiply', or 'divide'")

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)