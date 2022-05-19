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


# ================= Creating necessary variables ========================
# ------------------ Token, authentication variables ---------------------
SECRET_KEY = "4ab5be85c8c56eecdd547f7831979be83de58a6768d10a314f54cda4e4d67ffe"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ----------------- Database variables (MongoDB) --------------------------
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])
db = client.myTestDB