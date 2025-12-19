from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Settings(BaseModel):
    app_name: str = "My FastAPI App"
    admin_email: str = "admin@example.com"
    debug: bool = True


def get_settings() -> Settings:
    """
    Dependency provider that returns application settings.
    In a real app, this could read from env vars, config files, etc.
    """
    return Settings()

# GET API: Return configuration values using dependency injection
@app.get("/config", response_model=Settings)
def read_config(settings: Settings = Depends(get_settings)):
    return settings

# In-memory database for storing items by ID
items_db = {}

# Pydantic model for item validation
class Item(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

# Pydantic model for health check
class HealthStatus(BaseModel):
    status: str = "good"
    message: str = "web server is fine"

# GET API: Health check
@app.get("/health_check", response_model=HealthStatus)
def health_check():
    return HealthStatus()


# Fixed list of items for pagination demo
items_list = [
    Item(name="Laptop", description="Gaming laptop", price=1200.0, quantity=5),
    Item(name="Mouse", description="Wireless mouse", price=25.5, quantity=50),
    Item(name="Keyboard", description="Mechanical keyboard", price=75.0, quantity=20),
    Item(name="Monitor", description="24 inch monitor", price=150.0, quantity=15),
    Item(name="Headphones", description="Noise-cancelling headphones", price=200.0, quantity=10),
    Item(name="Webcam", description="HD webcam", price=60.0, quantity=30),
    Item(name="Microphone", description="USB microphone", price=90.0, quantity=25),
    Item(name="Chair", description="Ergonomic office chair", price=300.0, quantity=8),
    Item(name="Desk", description="Standing desk", price=400.0, quantity=6),
    Item(name="USB Hub", description="4-port USB 3.0 hub", price=35.0, quantity=40),
]


# GET API: Paginated list of items
@app.get("/items", response_model=list[Item])
def get_items(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, gt=0, description="Maximum number of items to return"),
):
    return items_list[skip : skip + limit]

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