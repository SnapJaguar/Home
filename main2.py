from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Модель данных для POST-запроса
class Item(BaseModel):
    name: str
    price: float

# GET-запрос (получение данных)
@app.get("/")
def read_root():
    return {"message": "Привет! Это твой REST сервис."}

# POST-запрос (отправка данных)
@app.post("/items/")
def create_item(item: Item):
    return {"status": "Успешно добавлено", "item_name": item.name, "total_price": item.price * 1.2}
