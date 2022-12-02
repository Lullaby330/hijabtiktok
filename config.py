import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5312133836:AAHm8esiRk3h4QcfqHedlA374wwsz5nYe4g")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6216349"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5c7418e9f3df6db931caa7354521c55f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001734154791"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5220678179"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://dreuggbyiywdvn:0b07592134a6cde27414a360b19164121a7c8ca4d303f9b48938802044f0b9f7@ec2-54-162-51-201.compute-1.amazonaws.com:5432/demapkme600pb1")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001554135295"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001739942775"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "{first} Kamu Harus Join Channel Dan Grup Terlebih Dahulu Ya Sebelum Melihat File Video ini.

Tutorial :
-[1.  Klik Start Bot
-[2. Join Channel & Group⬇️
-[3. Try Again dan Start
-I4. Tunggu hingga Video nya Muncul
-[5. Selamat Menikmati Asupan nya

Note :
Jangan spam ya karna bisa membuat bot delayed.
Sekian dan Terima Kasih.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5220678179").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hai {first} Kamu Harus Join Channel Dan Grup Terlebih Dahulu Ya Sebelum Melihat File Video ini.

Tutorial :
-[1. Wajib Join Channel & Group⬇️ :
     * https://t.me/+yxKqV1nBGB4xZTY9
     * https://t.me/+jb8dSWXy2ak2OWY1
-[2. Klik Coba Lagi dan Start
-[3. Tunggu hingga Video nya Muncul
-[4. Selamat Menikmati Asupan nya

Note :
Jangan spam ya karna bisa membuat bot delayed.
Sekian dan Terima Kasih.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
