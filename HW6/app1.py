from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
import sqlalchemy 
from sqlalchemy import Column, Table
import uvicorn
import databases
import datetime
from typing import List
from faker import Faker

fake = Faker()

DATABASE_URL = "sqlite:///./mydb.db"
db = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = Table(
"users",
metadata,
Column("user_id", sqlalchemy.Integer,
primary_key=True),
Column("name", sqlalchemy.String(32)),
Column("last_name", sqlalchemy.String(32)),
Column("birthday", sqlalchemy.Date()),
Column("email", sqlalchemy.String(128)),
Column("adress", sqlalchemy.String(128))
)



app = FastAPI()


engine = sqlalchemy.create_engine(
DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)


class UserIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=32)
    last_name: str = Field(..., min_length=2, max_length=32)
    birthday: datetime.date
    email: str = EmailStr
    adress: str = Field(None, min_length=5, max_length=128)

class User(BaseModel):
    user_id:int
    name: str = Field(..., min_length=2, max_length=32)
    last_name: str = Field(..., min_length=2, max_length=32)
    birthday:datetime.date
    email: str = EmailStr
    adress: str = Field(None, min_length=5, max_length=128)


@app.on_event("startup")
async def startup():
    return db.connect()

@app.on_event("shutdown")
async def shutdown():
    return db.connect()

@app.get("/fake_users/{count}")
async def create_fake_users(count: int):
    for i in range(count):
        query = users.insert().values(name=fake.first_name(),last_name=fake.last_name(), birthday = fake.date_of_birth(),  email=fake.email(), adress = fake.address())
        await db.execute(query)
    return {'message': f'{count} пользователей создано'}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await db.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id:int):
    query = users.select().where(users.c.user_id == user_id)
    return await db.fetch_one(query)

@app.post("/add_user/", response_model=UserIn)
async def read_user(user:UserIn):
    query = users.insert().values(**user.model_dump())
    last_id = await db.execute(query)
    return {**user.model_dump()}


@app.put("/add_user/{user_id}", response_model=User)
async def update_user(user_id:int, user:UserIn):
    query = users.update().where(users.c.user_id == user_id).values(**user.model_dump())
    await db.execute(query)
    return {**user.model_dump(), "user_id": user_id}

@app.delete("/delete_user/{user_id}")
async def delete_user(user_id:int):
    query = users.delete().where(users.c.user_id == user_id)
    await db.execute(query)
    return {'message': f'Пользователь удалён'}



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)