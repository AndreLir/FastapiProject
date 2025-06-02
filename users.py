from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server con el comando: uvicorn users:app --reload

# Entidad User
class User(BaseModel):
    # Atributos de la entidad User
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id=1, name="Brais", surname="Moure",  url="https://mouredev.dev",age=35),
         User(id=2, name="John", surname="Doe", url="https://example.com", age=30),
         User(id=3, name="Jane", surname="Smith", url="https://example.com", age=28)]  # Corregido aquí

@app.get("/usersJson")
async def usersJson():
    return [{"name":"Brais","surname":"Moure","url":"https://mouredev.dev","age":35},
            {"name":"John","surname":"Doe","url":"https://example.com","age":30},
            {"name":"Jane","surname":"Smith","url":"https://example.com","age":28}]
            
@app.get("/users")
async def usersClass():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# @app.get("/userquery/")
# async def user(id: int):
#     users = filter(lambda user: user.id == id, users_list)
#     try:
#         return list(users)[0]
#     except IndexError:
#         return {"error": "User not found"}, 404

@app.get("/user")
async def user(id: int):
        return search_user(id)    

@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id))== User:
        return {"error": "User already exists"}
    else: 
        users_list.append(user)

@app.put("/user/")
async def user(user: User):
    
    found= False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return user
    if not found:
        return {"error": "User not found"}, 404        


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "User not found"}, 404
    
