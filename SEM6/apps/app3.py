import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description:Optional[str] = None
    price: float
    tax: Optional[float] = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/items/{item_id}")
async def read_root(item_id:int, q: str = None):
    if q:
        return {"item_id": item_id, "q":q}
    
    return {"item_id":item_id}

# @app.post("/items/")
# async def create_item(item:Item):
#     logger.info('Отработал запрос')
#     return item