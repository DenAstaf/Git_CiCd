"""
Данный модуль выполняет:
Создает экземпляр приложения FastAPI.
Настраивает шаблонизатор Jinja2.
Определяет маршруты
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Настраиваем шаблонизатор Jinja2, указывая директорию для шаблонов
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    """Определяет маршрут корневого пути"""
    return 'Hello, World!'


@app.get("/json")
def read_json():
    """Определяет маршрут, возвращающий JSON ответ"""
    return {"message": "Hello, World in JSON!"}


@app.get("/html", response_class=HTMLResponse)
def read_templated_html(request: Request):
    """Определяет маршрут, использующий шаблон Jinja2 для формирования ответа"""
    context = {
        "title": "Hello, Templated World!",
        "message": "Hello, World in HTML with Templating!",
    }
    return templates.TemplateResponse(request, "step_1.html", context)


@app.get("/query")
def read_query_string(name: str):
    """Определяет маршрут, возвращающий ответ с использованием query строки"""
    return {"message": f"Hello, my name is {name}!"}
