import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8334353"))
API_HASH = getenv("API_HASH", "4cf512e6f3274086dd6364a952b9a094")
BOT_USERNAME = getenv("BOT_USERNAME", "FULL_MOJJ_MASTI_BOT")
BOT_TOKEN = getenv("BOT_TOKEN", "5362313685:AAGemPJYpaht90eSsh5ssz_WN999jUXU-YU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQAyOC6TJv6iQrU2Xo-NOuym9gRs7dw0qfx13Q6l5Kh_zHfA26r4vlioFnEkvLgZqxw3wNbkP1SCNT14QpvOZ6gllf6B4DwBYTeRJlSqDu2EUnRcbVElZBWcmMlEwVYIIn6NUvCuBr94nw0VZc8KXjVBLyxttOCpqe44tVPyROHCz7sEPnohM-yDZkiN8CsbpN3fLyrpyhEfUmng-Ou_rGdLvd-UQYbBsshTna8ywNtMKHuoXvcPi9RKsCU_5Y7d_KFZsFwin2nObAJBzbkHNdCW2alvKcTo9mrNEUT5O6-cKcbaZ77WVKR34MIbgnddYkQgusKu_Gcq3RT6WI5r5Ip4AAAAATQaCA8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
aiohttpsession = aiohttp.ClientSession()
