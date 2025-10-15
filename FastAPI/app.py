from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, EmailStr

app = FastAPI() 

itens = [] # array in memory

class Item(BaseModel):
    id: int # definição do tipo de dado para numero inteiro, será incremental
    name: str # definição do tipo de dado para string
    email: EmailStr # definição do tipo de dado para email valido, validado pelo Pydantic

@app.get("/itens") # endpoint com get/itens
def get_itens():
    return itens # returning the itens list

@app.get("/itens/{item_id}") # endpoint with get/itens/id to find a specifc ID
def get_id(item_id: int): # using the ID with parameter
    for item in itens: # loop 
        if item.id == item_id:
            return item # 200 OK automatic
    raise HTTPException(status_code=404, detail="Item not found") # error message
