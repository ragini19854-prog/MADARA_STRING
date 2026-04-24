from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "35411328"))
API_HASH = getenv("API_HASH", "4c8d3c8f5d3483296f5fb530ea2cfcc6")

BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "8441236350"))

MONGO_DB_URI = getenv("mongodb+srv://ragini19854_db_user:madaraadamuchiha@madara.iuvs13y.mongodb.net/madara?retryWrites=true&w=majority&appName=MADARA")
MUST_JOIN = getenv("MUST_JOIN", "MADARA_GMS")
