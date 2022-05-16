#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# @File: main
# @Author: Cherni Oussama
# @Time: 16/05/2022 08:59
# @Contact :   oussama.cherni@ensi-uma.tn
# ---------------------------------------------------------------------------
import json

import uvicorn
from fastapi import FastAPI, Response
from scraper import FacebookScraper
from utils import *


app = FastAPI()


@app.get("/")
async def root():
    page_name = "TED"

    scraper_fb = FacebookScraper(page_name, 50)
    scraper_fb.init_driver()
    scroll_to_bottom(scraper_fb.driver, 8)
    data = scraper_fb.scrape_data()

    json_data = json.dumps(data, indent=4)
    return Response(content=json_data, media_type="application/json")


if __name__ == "__main__":
    uvicorn.run(app='main:app')

