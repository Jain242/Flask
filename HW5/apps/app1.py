from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
from pydantic import BaseModel, EmailStr, constr

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    user_id : int
    name:str
    email: EmailStr
    password:constr(min_length=8, max_length=16)

users:List[User] =[]
for i in range(10):
    user_id=i
    name= "name_"+str(i)
    email = "mail" +str(i)+"@mail.ru"
    password="1234567890"+str(i)
    data={"user_id":user_id, "name":name,"email":email, "password":password}
    user=User(**data)
    users.append(user)

print (users)


@app.get("/users/")
def get_user():
    return {"task_list":users}
    

@app.post("/add_user/")
def create_user(user: User):
    users.append(user)
    return {"users":users}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    users[user_id]=user
    return {"user_id":user_id, "user":user}



@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for u in users:
        if u.user_id ==user_id:
            users.remove(u)
    return {"user_id":user_id}

@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "users": users})