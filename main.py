import uvicorn
from fastapi import FastAPI, HTTPException

from app.models import User
from app.repositories import create_user, update_user
from app.schemas import UserRetrieveSchema, UserUpdateSchema

app = FastAPI()


@app.get("/")
def root():
    return "hello world!"


@app.get("/user", response_model=UserRetrieveSchema)
def get_user():
    user = User.objects().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/user", response_model=UserRetrieveSchema)
def post_user(token: str, user_schema: UserUpdateSchema):
    user = create_user(token, user_schema)
    return user


@app.put("/user", response_model=UserRetrieveSchema)
def put_user(token: str, user_schema: UserUpdateSchema):
    user = update_user(token, user_schema)
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
