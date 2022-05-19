#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# @File: utils
# @Author: Cherni Oussama
# @Time: 16/05/2022 09:14
# @Contact :   oussama.cherni@ensi-uma.tn
# ---------------------------------------------------------------------------

import os
import re
import time
import zipfile
from random import randint
from sys import platform

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests


def get_os_system():
    if platform == "linux" or platform == "linux2":
        print("linux")
    elif platform == "darwin":
        print("darwin")
    elif platform == "win32":
        print("Windows")


def download_chrome_driver():
    cwd = os.getcwd()
    folder_driver_path = os.path.join(cwd, "driver")
    driver_path = os.path.join(cwd, "driver", "chromedriver.exe")

    if platform == "linux" or platform == "linux2":
        chrome_type = "chromedriver_linux64"
    elif platform == "win32":
        chrome_type = "chromedriver_win32"

    if not os.path.exists(driver_path):
        if not os.path.isdir(folder_driver_path):
            os.mkdir("driver")
            if chrome_type == "chromedriver_win32":
                os.system('cmd /c "curl https://chromedriver.storage.googleapis.com/101.0.4951.41/{}.zip > '
                  '{}"'.format(chrome_type, (os.path.join(folder_driver_path, "chrome_driver.zip"))))
                with zipfile.ZipFile(os.path.join(folder_driver_path, "chrome_driver.zip"), 'r') as zip_ref:
                    zip_ref.extractall(folder_driver_path)
                os.remove(os.path.join(folder_driver_path, "chrome_driver.zip"))

            else:
                os.system("wget -N http://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip")
                os.system("unzip chromedriver_linux64.zip")
                os.system("chmod +x chromedriver")
                os.system("mv -f chromedriver /usr/local/share/chromedriver")
                os.system("ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver")
                os.system("ln -s /usr/local/share/chromedriver /usr/bin/chromedriver")

    else:
        print("Chrome driver exists ! ")


def initialize_driver():
    if platform == "linux" or platform == "linux2":
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en")
        options.binary_location = "/usr/bin/google-chrome"  # chrome binary location specified here
        options.add_argument("--start-maximized")  # open Browser in maximized mode
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")  # bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(r'/usr/local/share/chromedriver', options=options)
    else:
        cwd = os.getcwd()
        driver_path = os.path.join(cwd, "driver", "chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en")
        options.add_argument('--headless')
        options.add_argument("--start-maximized")  # open Browser in maximized mode
        options.add_argument("--no-sandbox")  # bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(driver_path, options=options)

    return driver


def get_full_path(tag):
    return "https://facebook.com/{}".format(tag)


def get_name(driver):
    name = driver.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
    return name


def close_error_popup(driver):
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label=Close]")))
        driver.find_element(By.CSS_SELECTOR, "[aria-label=Close]").click()

    except WebDriverException as e:
        try:
            time.sleep(5)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label=Close]")))
            driver.find_element(By.CSS_SELECTOR, "[aria-label=Close]").click()
        except WebDriverException as e:
            pass

    except Exception as ex:
        pass
        print("error at close_error_popup method : {}".format(ex))


def scroll_down_first(driver):
    body = driver.find_element(By.CSS_SELECTOR, "body")
    for _ in range(randint(5, 6)):
        body.send_keys(Keys.PAGE_UP)
    for _ in range(randint(5, 8)):
        body.send_keys(Keys.PAGE_DOWN)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def check_timeout(start_time, current_time, timeout):
    return (current_time - start_time) > timeout


def scroll_to_bottom(driver, timeout):
    old_position = 0
    new_position = None
    end_position = 0
    start_time = time.time()
    body = driver.find_element(By.CSS_SELECTOR, "body")

    while new_position != old_position and not check_timeout(start_time, time.time(), timeout):
        # Get old scroll position
        old_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(1)
        driver.execute_script((
            "var scrollingElement = (document.scrollingElement ||"
            " document.body);scrollingElement.scrollTop ="
            " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))

        if end_position != new_position:
            for _ in range(randint(5, 6)):
                body.send_keys(Keys.PAGE_UP)
        end_position = new_position
    if new_position == old_position:
        print("All")
    else:
        print("Timeout")


def get_text(post):
    try:
        div_text = post.find_element(By.CSS_SELECTOR, '[data-ad-comet-preview]')
        text = div_text.get_attribute('innerText')
    except:
        text = None
    return text


def get_link_video(post):
    try:
        div_text = post.find_element(By.CSS_SELECTOR, "[aria-label='Enlarge']")
        text = div_text.get_attribute('href')
        text = text[:text.rfind("/")]
    except:
        text = None
    return text


def get_shares_comments(post):
    elements = post.find_elements(By.CSS_SELECTOR, "div.gtad4xkn")
    shares = "0"
    comments = "0"
    for element in elements:
        text = element.get_attribute("innerText")
        if "Shares" in text:
            shares = re.findall("\d+", text)[0]

        if "Comments" in text:
            comments = re.findall("\d+", text)[0]

    return shares, comments


def get_reactions(post):
    reactions = 0
    try:
        total_reactions = post.find_element(By.CSS_SELECTOR, 'span.ltmttdrg.gjzvkazv')
        reactions = total_reactions.get_attribute("innerText")
    except Exception as e:
        print(e)
    return reactions


def get_posted_time(post):
    element = post.find_element(By.CSS_SELECTOR, "a.gpro0wi8.b1v8xokw")
    print(element.get_attribute('innerText'))


def get_images(post):
    list_of_images = []
    elements = post.find_elements(By.CSS_SELECTOR, 'div.do00u71z.ni8dbmo4.stjgntxs.l9j0dhe7 img.i09qtzwb')
    for element in elements:
        list_of_images.append(element.get_attribute('src'))
    return list_of_images


def check_page_exists(name):
    url = "https://graph.facebook.com/" + name
    response = requests.get(url)

    if (response.text.find("Unsupported get request") == -1):
        return True
    else:
        return False
