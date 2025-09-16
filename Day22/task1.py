from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        return value

@app.post("/products/")
def create_product(product: Product):
    return {"message": "Product created successfully", "product": product}
