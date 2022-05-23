#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# @File: main
# @Author: Cherni Oussama
# @Time: 16/05/2022 08:59
# @Contact :   oussama.cherni@ensi-uma.tn
# ---------------------------------------------------------------------------

import uvicorn
from fastapi import FastAPI
from routers.router import router
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# ================= Routers inclusion ===============
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app='main:app')
