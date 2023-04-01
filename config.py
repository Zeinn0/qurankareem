from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9000"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/4921b5d12ac8f7013ac73.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/4921b5d12ac8f7013ac73.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/D_FBJ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/pp_g3")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5190136458").split()))


FAILED = "https://graph.org/file/4921b5d12ac8f7013ac73.jpg"
