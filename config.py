#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# @File: config
# @Author: Cherni Oussama
# @Time: 20/05/2022 16:40
# @Contact :   oussama.cherni@ensi-uma.tn
# ---------------------------------------------------------------------------

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import motor.motor_asyncio
import os


# ----------------- Database variables (MongoDB) --------------------------
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])
db = client.myTestDB
