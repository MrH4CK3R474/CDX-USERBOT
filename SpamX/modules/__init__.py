from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "🇨Ⓞ𝗗𝜩🇽"
pic = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/0d7c524a3fe2798398b3a.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐎𝐏 ѕραм - by 𝗖ⓞ𝗗𝜩𝗫"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**[☆𝗖ⓞ𝗗𝜩𝗫☆](https://t.me/TEAM_CDX)
◈ •━━━━━★✦♡✦★━━━━━• ◈
➪ **𝗠𝚲𝗦𝗧𝜩𝗥:**[☆𝗞𝚲𝐌𝜩𝜩𝐍𝚲☆](https://t.me/BRANDED_KAMEENAA)
◈ •━━━━━━━★━━━━━━━• ◈ 
➪ **𝗗єѵʅ𝕆թєƦ:**[☆𝚲𝗟Ⓞ𝗡𝜩☆](https://t.me/reallyaloneboy_01)
➪ **𝗣ƴƬнοи ⩔єяនɨ០ɳ:** `{platform.python_version()}`
➪ **𝗖ⓞ𝗗𝜩 ⩔єяនɨ០ɳ:** `{__version__}`
➪ **𝗣ƴяο ⩔єяនɨ០ɳ:** `{pyro_vr}`
◈ •━━━━━★✦♡✦★━━━━━• ◈
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
