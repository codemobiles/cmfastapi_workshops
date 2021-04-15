# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
from typing import Optional
from fastapi import FastAPI
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# password = "1234"
# hashed_password = get_password_hash(password) 
# print(hashed_password)

# if verify_password(password+"x", hashed_password):
#     print("password is correct")
# else:
#     print("password is incorrect")    

users = {}

@app.get("/register")
def register(username:str, password:str):
    users[username] = get_password_hash(password)
    return users


@app.get("/login")
def login(username:str, password:str):
    try:
        hashed_password = users[username]    
        if verify_password(password, hashed_password):
            return {"login":"ok"}
        else: 
            return {"login": "nok - invalid password"}
    except:
        return {"login": "nok - invalid username"}