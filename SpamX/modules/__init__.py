from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "🇨Ⓞ𝗗𝜩🇽"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/a04b4a2e69f81f60c4599.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else ""

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[𝗞𝚲𝐌𝜩𝜩𝐍𝚲](tg://BRANDED_KAMEENAA)"

class Alive:
     Pic = pic
     
     msg = f"""
ALT = f"""➪**[★ 🇨Ⓞ𝗗𝜩🇽 ★]
☆━━━━━━★✦★✦★━━━━━━☆
➪ 𝐏𝐘𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :-  {platform.python_version()}
➪ 𝐂𝐎𝐃𝐄 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :- {version}
➪ 𝐏𝐘𝐑𝐎 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :- {pyro_vr}
☆━━━━━━★✦★✦★━━━━━━☆
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
