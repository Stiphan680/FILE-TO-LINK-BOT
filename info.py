from os import environ, getenv
from Script import script

# 🚀 Bot Configuration
SESSION = environ.get('SESSION', 'FileToLinkBot')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# 👑 Owner & Admins
ADMINS = [int(i) for i in environ.get('ADMINS', '').split()] if environ.get('ADMINS') else []
AUTH_CHANNEL = [int(i) for i in environ.get("AUTH_CHANNEL", "").split()] if environ.get("AUTH_CHANNEL") else []
OWNER_USERNAME = environ.get("OWNER_USERNAME", '')
BOT_USERNAME = environ.get("BOT_USERNAME", '')

# 🔗 Channel & Support Links
CHANNEL = environ.get('CHANNEL', '')
SUPPORT = environ.get('SUPPORT', '')

# 📢 Log Channels (Simplified - only essential)
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '0')) if environ.get("BIN_CHANNEL") else 0
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '0')) if environ.get("LOG_CHANNEL") else 0

# ✅ Feature Toggles (Simplified)
VERIFY = False  # Disabled
FSUB = environ.get("FSUB", "False").lower() == "true"  # Force Subscribe - optional
ENABLE_LIMIT = False  # Disabled
BATCH_VERIFY = False  # Disabled
IS_SHORTLINK = False  # Disabled
MAINTENANCE_MODE = False  # Disabled
PROTECT_CONTENT = environ.get('PROTECT_CONTENT', "False").lower() == "true"
PUBLIC_FILE_STORE = True  # Always enabled
BATCH_PROTECT_CONTENT = False

# 🔗 Shortlink Configuration (Disabled)
SHORTLINK_URL = ''
SHORTLINK_API = ''

# 💾 Database Configuration
DB_URL = environ.get('DATABASE_URI', "")
DB_NAME = environ.get('DATABASE_NAME', "filetolinkbot")

# 📸 Media & Images (Optional)
QR_CODE = environ.get('QR_CODE', '')
VERIFY_IMG = environ.get("VERIFY_IMG", "")
AUTH_PICS = environ.get('AUTH_PICS', '')
PICS = environ.get('PICS', '')
FILE_PIC = environ.get('FILE_PIC', '')

# 📝 Captions
FILE_CAPTION = environ.get('FILE_CAPTION', script.CAPTION)
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', script.CAPTION)
CHANNEL_FILE_CAPTION = environ.get('CHANNEL_FILE_CAPTION', script.CAPTION)

# ⏱️ Time & Limits
PING_INTERVAL = int(environ.get("PING_INTERVAL", 1200))
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', 60))
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", 600))
MAX_FILES = int(environ.get("MAX_FILES", 50))

# ⚙️ Worker & App Config
WORKERS = int(environ.get('WORKERS', 10))
MULTI_CLIENT = False
NAME = environ.get('name', 'filetolinkbot')

# 🌐 Web Server
ON_HEROKU = 'DYNO' in environ
APP_NAME = environ.get('APP_NAME') if ON_HEROKU else None

PORT = int(environ.get('PORT', 8080))
NO_PORT = str(environ.get("NO_PORT", "true")).lower() in ("true", "1", "yes")
HAS_SSL = str(environ.get("HAS_SSL", "true")).lower() in ("true", "1", "yes")

# URL Generation
BIND_ADDRESS = environ.get("WEB_SERVER_BIND_ADDRESS", "")
FQDN = environ.get("FQDN", BIND_ADDRESS)

if FQDN and not FQDN.startswith("http"):
    PROTOCOL = "https" if HAS_SSL else "http"
    PORT_SEGMENT = "" if NO_PORT else f":{PORT}"
    FQDN = FQDN.rstrip('/')
    URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"
elif FQDN:
    URL = FQDN
else:
    URL = ""

# 🔄 Backward Compatibility (for old plugin files)
VERIFIED_LOG = LOG_CHANNEL  # Use LOG_CHANNEL for verified user logs
VERIFY_EXPIRE = 3600  # Default expire time in seconds (1 hour)
