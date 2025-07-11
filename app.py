from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from agents import Agent, AsyncOpenAI,OpenAIChatCompletionsModel,Runner


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# ✅ About route
@app.get("/", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        request=request, name="shop.html", context={"name": "Maria"}
    )
