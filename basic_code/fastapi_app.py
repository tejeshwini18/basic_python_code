from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# In-memory database for storing items
items_db = {}

# Pydantic model for item validation
class Item(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

# GET API: Retrieve an item by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# POST API: Create a new item
@app.post("/items/", response_model=Item)
def create_item(item: Item, item_id: int = Query(..., description="The unique ID for the item.")):
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items_db[item_id] = item
    return item

# PUT API: Update an existing item by ID
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item

# DELETE API: Delete an item by ID
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}

if __name__=='__main__':
    uvicorn.run(app)