#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2024-09-08 23:09:45
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={"id": id},
    )


@app.get("/doc", response_class=HTMLResponse)
async def doc(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="doc.html",
        context={},
    )


@app.put("/messages", response_class=HTMLResponse)
async def messages(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="messages.html",
        context={},
    )
