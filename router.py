#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# @File: router
# @Author: Cherni Oussama
# @Time: 21/05/2022 11:39
# @Contact :   oussama.cherni@ensi-uma.tn
# ---------------------------------------------------------------------------
from config import db
from scraper import FacebookScraper
from utils import *
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request, 'result': ""})


@router.post("/")
async def form_post(request: Request, name: str = Form(...), timeout: int = Form(...)):
    result = check_page_exists(name)
    if not result:
        return templates.TemplateResponse('form.html', context={'request': request, 'result': "There is no page "
                                                                                              "named {}".format(name)})
    else:
        scraper_fb = FacebookScraper(name, timeout)
        scraper_fb.init_driver()
        scroll_to_bottom(scraper_fb.driver, 8)
        data = scraper_fb.scrape_data()

        for i in range(len(data)):
            rec = await db[name].insert_one(data[i])

        pages = await db[name].find().to_list(1000)
        docs = []
        for doc in pages:
            doc.pop('_id')
            docs.append(doc)
        return templates.TemplateResponse('table.html', context={'request': request, 'title': name, 'posts': docs})


@router.get("/list")
async def list_all_collections(request: Request):
    collections = await db.list_collection_names()

    return templates.TemplateResponse('collections_table.html', context={'request': request, 'title': "ALL SCRAPPED "
                                                                                                      "PAGES",
                                                                         'collections': collections})


@router.get("/list/{page_name}")
async def display_collection(request: Request, page_name):

    pages = await db[page_name].find().to_list(1000)
    docs = []
    for doc in pages:
        doc.pop('_id')
        docs.append(doc)
    return templates.TemplateResponse('table.html', context={'request': request, 'title': page_name, 'posts': docs})
