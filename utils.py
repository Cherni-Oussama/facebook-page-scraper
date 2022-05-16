#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# @File: utils
# @Author: Cherni Oussama
# @Time: 16/05/2022 09:14
# @Contact :   oussama.cherni@ensi-uma.tn
# ---------------------------------------------------------------------------

import os
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def download_chrome_driver():
    cwd = os.getcwd()
    folder_driver_path = os.path.join(cwd, "driver")
    driver_path = os.path.join(cwd, "driver", "chromedriver.exe")
    if not os.path.exists(driver_path):
        if not os.path.isdir(folder_driver_path):
            os.mkdir("driver")
        os.system('cmd /c "curl https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_win32.zip > '
                  '{}"'.format(str(os.path.join(folder_driver_path, "chrome_driver.zip"))))
        with zipfile.ZipFile(os.path.join(folder_driver_path, "chrome_driver.zip"), 'r') as zip_ref:
            zip_ref.extractall(folder_driver_path)
        os.remove(os.path.join(folder_driver_path, "chrome_driver.zip"))
    else:
        print("Chrome driver exists ! ")

def initialize_driver():
    cwd = os.getcwd()
    driver_path = os.path.join(cwd, "driver", "chromedriver.exe")
    options = Options()
    options.headless = False
    options.add_argument('lang=en')
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(driver_path, options=options)
    return driver
