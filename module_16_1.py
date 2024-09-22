from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def welcome() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def number(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def info(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

#python3 -m uvicorn module_16_1:app