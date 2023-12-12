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
   owner_mention = f"[𝗞𝚲𝐌𝜩𝜩𝐍𝚲](tg://BRANDED_KAMEENAA)"

class Alive:
     Pic = pic
     
     msg = f"""
**[★🇨Ⓞ𝗗𝜩🇽★](https://t.me/TEAM_CDX)
☆━━━━━━━★✦★✦★━━━━━━━☆
★ **𝗠𝚲𝗦𝗧𝜩𝗥:-**[☆ 𝗞𝚲𝐌𝜩𝜩𝐍𝚲 ☆](https://t.me/BRANDED_KAMEENAA)
   ☆━━━━━━━★━━━━━━━☆ 
➪ **𝗣𝗬𝗧𝗛𝚹𝗡 ⩔𝗘𝗥𝗦𝗜𝚹𝗡:-** `{platform.python_version()}`
➪ **𝗖𝚹𝗗𝜩  ⩔𝗘𝗥𝗦𝗜𝚹𝗡:-** `{__version__}`
➪ **𝗣𝗬𝗥𝚹  ⩔𝗘𝗥𝗦𝗜𝚹𝗡:-** `{pyro_vr}`
☆━━━━━━━★✦★✦★━━━━━━━☆
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
