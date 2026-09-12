from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Dict, Annotated

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    weight: Annotated[int, Field(lt=100)]

@app.get("/")
def home():
    return {"Message": "SUCCESS"}

@app.post("/about")
def about(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "weight": student.weight
    }

