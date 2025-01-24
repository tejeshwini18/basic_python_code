from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

cor_origin = ["http://127.0.0.1/8000"]


class datavalidation(BaseModel):
    status: str
    message: str = "web server is fine"


app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins = cor_origin,
                   allow_credentials=True,
                   allow_methods = ['GET','POST'])

@app.get("/health_check",response_model=datavalidation)
def healthcheck():
    return datavalidation(status="good")

if __name__ == '__main__':
    uvicorn.run(app)