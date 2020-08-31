from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

from algorithms_code import algorithms_element_unique as alg

class Item(BaseModel):
    # N: int
    # K: List[int]
    input:List[int]


app = FastAPI()


@app.get("/")
def root():
    return "API-V1"


@app.post("/uniqueElements/")
def verify_unique_elements(item: Item):
    N = item.input[0]
    list_K =item.input[1:len(item.input)]

    print(alg.unique_elements(list_K, N))

    return {"output":alg.unique_elements(list_K, N)}