from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return {"items": items}

@app.post("/items")
def add_item(item: str):
    items.append(item)
    return {"message": "added", "item": item}
