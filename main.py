#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# @File: main
# @Author: Cherni Oussama
# @Time: 16/05/2022 08:59
# @Contact :   oussama.cherni@ensi-uma.tn
# ---------------------------------------------------------------------------

from utils import *


if __name__ == "__main__":
    download_chrome_driver()
    driver = initialize_driver()
    driver.quit()
