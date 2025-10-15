from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, EmailStr

app = FastAPI() 

itens = [] # Variavel global, banco de dados em memoria (lista para itens)

class Item(BaseModel):
    id: int # definição do tipo de dado para numero inteiro, será incremental
    name: str # definição do tipo de dado para string
    email: EmailStr # definição do tipo de dado para email valido, validado pelo Pydantic

@app.get("/itens") #endpoint com Get(/itens)
def get_itens():
    return itens #returning the itens list
