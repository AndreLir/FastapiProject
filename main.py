from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI"

@app.get("/url")
async def url():
    return {"url_curso":"https://mouredev.com/python"}

#La documentacion esta en http://localhost:8000/docs
#tambien se puede acceder a la documentacion en http://localhost:8000/redoc

