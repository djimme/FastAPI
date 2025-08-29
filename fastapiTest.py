from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Pydantic 데이터 모델 선언
class User(BaseModel):
    name : str
    email : str

# 인메모리 데이터 저장소
users: Dict[int, User] = {
    1: User(name = "Alice", email ="alice@example.com"),
    2: User(name = "Bob", email ="bob@example.com")
}

# 전체 사용자 조회 (GET)
@app.get("/users")
def list_users():
    return users

# 특정 사용자 조회 (GET)
@app.get("/users/{uid}")
def get_user(uid: int):
    if uid in users:
        return users[uid]
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
# 새 사용자 추가(POST)
@app.post("/users", status_code=201)
def create_user(user: User):
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = user
    return {"id": new_id, **user.model_dump(mode="json")}

# 사용자 정보 수정(PUT)
@app.put("/users/{uid}")
def update_user(uid: int, user: User):
    if uid in users:
        users[uid] = user
        return {"id": uid, **user.model_dump()}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
# 사용자 삭제(DELETE)
@app.delete("/users/{uid}")
def delete_user(uid: int):
    if uid in users:
        del users[uid]
        return {"result": "user deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")