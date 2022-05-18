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
from fastapi import FastAPI, Response, Request, Form
from fastapi.templating import Jinja2Templates

from scraper import FacebookScraper
from utils import *

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/")
def form_post(request: Request):
    result = "Type a facebook page name"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': ""})


@app.post("/")
def form_post(request: Request, name: str = Form(...)):
    result = check_page_exists(name)
    if not result:
        return templates.TemplateResponse('form.html', context={'request': request, 'result': "There is not page "
                                                                                              "named {}".format(name)})
    else:
        page_name = "TED"
        download_chrome_driver()
        scraper_fb = FacebookScraper(page_name, 100)
        scraper_fb.init_driver()
        scroll_to_bottom(scraper_fb.driver, 8)
        data = scraper_fb.scrape_data()
        json_data = json.dumps(data, indent=4)

        # data = scraper_fb.get_data()
        return Response(content=json_data, media_type="application/json")


if __name__ == "__main__":
    uvicorn.run(app='main:app')

