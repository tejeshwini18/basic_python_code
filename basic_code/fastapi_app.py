from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/home")
def home():
    return {"message":"Hello,Welcome to my fastapi web application"}


if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0',port=8000,reload=True)