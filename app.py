from fastapi import FastAPI, Request, Form
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.model import PlagiaGuard

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def load_form(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def respond_form(request: Request, code: str = Form(...)):
    pg = PlagiaGuard(code)
    results = pg.table_output()
    return templates.TemplateResponse("response.html", {"request": request, "html_table": results})

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)