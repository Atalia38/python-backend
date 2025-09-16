from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to our API."}
