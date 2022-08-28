import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '15430744'))
API_HASH = environ.get('API_HASH', '9029b7d66c1cb94805dfb77774e5abba')
BOT_TOKEN = environ.get('BOT_TOKEN', '5470181920:AAFRt6jCpkLR1KbJSxh3K8WOY9N4h3U752s')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', "https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg")).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '761686219 1875429051 1369291772').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001795586205 -1001795586205", '-1001795586205 -1001795586205').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://rai:rai@cluster0.zcrha.mongodb.net/?retryWrites=true&w=majority')
DATABASE_NAME = environ.get('DATABASE_NAME', 'Gofilefhjrobot')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001729830342'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'rai_info17')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'True')), False)
IMDB = is_enabled((environ.get('IMDB', 'True')), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', 'True')), False)
CUSTOM_FILE_CAPTION = environ.get('CUSTOM_FILE_CAPTION', '🗂 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘: <code>PIRO|{file_name}</code> \n📥 𝗙𝗜𝗟𝗘 𝗦𝗜𝗭𝗘: <i>{file_size}</i> \n❤️‍🔥 𝗝𝗢𝗜𝗡 [𝗕𝗟𝗔𝗦𝗧𝗘𝗥 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 ;)](https://t.me/blasters_monthly)  \n😌 𝗥𝗘𝗤𝗨𝗘𝗦𝗧𝗦 - ||@raixpiro_bot|| \n🎊[『ᴘɪʀᴏ』](https://t.me/rai_info17)')
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', '🗂 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘: <code>PIRO|{file_name}</code> \n📥 𝗙𝗜𝗟𝗘 𝗦𝗜𝗭𝗘: <i>{file_size}</i> \n❤️‍🔥 𝗝𝗢𝗜𝗡 [𝗕𝗟𝗔𝗦𝗧𝗘𝗥 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 ;)](https://t.me/blasters_monthly)  \n😌 𝗥𝗘𝗤𝗨𝗘𝗦𝗧𝗦 - ||@raixpiro_bot|| \n🎊[『ᴘɪʀᴏ』](https://t.me/rai_info17)')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', '🏷 𝖳𝗂𝗍𝗅𝖾: {title} \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10  \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [『ᴘɪʀᴏ』](t.me/rai_info17)')
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
