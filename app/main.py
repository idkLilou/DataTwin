from fastapi import FastAPI, HTTPException

from app.calculator import Calculator

app = FastAPI(title="Calculator API")


@app.get("/")
def root():
    return {"message": "Calculator API"}


@app.get("/add")
def add(a: float, b: float):
    return {"result": Calculator.add(a, b)}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": Calculator.subtract(a, b)}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": Calculator.multiply(a, b)}


@app.get("/divide")
def divide(a: float, b: float):
    try:
        return {"result": Calculator.divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
