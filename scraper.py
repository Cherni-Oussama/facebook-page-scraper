#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# @File: scraper
# @Author: Cherni Oussama
# @Time: 16/05/2022 09:13
# @Contact :   oussama.cherni@ensi-uma.tn
# ---------------------------------------------------------------------------

import json
from utils import *
from selenium.webdriver.common.by import By


class FacebookScraper:
    data_dict = {}

    def __init__(self, page_name, timeout):
        self.page_name = page_name
        self.URL = get_full_path(page_name)
        self.driver = None
        self.timeout = timeout

    def init_driver(self):
        download_chrome_driver()
        self.driver = initialize_driver()
        self.driver.get(self.URL)
        scroll_down_first(self.driver)
        close_error_popup(self.driver)

    def scrape_data(self):
        all_posts = self.driver.find_elements(By.CSS_SELECTOR, '[aria-posinset]')
        for index, post in enumerate(all_posts):
            id_ = index
            text = get_text(post)
            video = get_link_video(post)
            shares, comments = get_shares_comments(post)
            total_reactions = get_reactions(post)
            posted_time = get_posted_time(post)
            images = get_images(post)

            self.data_dict[id_] = {
                "page_name": self.page_name,
                "shares": shares,
                "reaction_count": total_reactions,
                "comments": comments,
                "content": text,
                "posted_on": posted_time,
                "video": video,
                "image": images,
            }
        # json_data = json.dumps(self.data_dict, indent=4)
        return self.data_dict
