# fastapi-twitter
pgadmin4: 
http://localhost:8080/pgadmin4/browser/
change port:
find: sudo find /usr/pgadmin4 -name "config.py"

Create: /usr/pgadmin4/web/config_local.py

###############################################################
# Custom pgAdmin4 Local Configuration (Safe for Global Access)
###############################################################

# Run pgAdmin on all network interfaces so you can access via LAN
DEFAULT_SERVER = '0.0.0.0'

# Web UI Port (change if 8080 collides)
DEFAULT_SERVER_PORT = 8080

# CSRF: keep enabled normally
CSRF_ENABLED = True

# Internal SQLite DB for pgAdmin metadata (users, servers)
SQLITE_PATH = '/var/lib/pgadmin/pgadmin4.db'

# Logs
LOG_FILE = '/var/log/pgadmin4/pgadmin4.log'

# Session & storage
SESSION_DB_PATH = '/var/lib/pgadmin/sessions'
STORAGE_DIR = '/var/lib/pgadmin/storage'

# Allow saving DB passwords in pgAdmin
ALLOW_SAVE_PASSWORD = True

# Optional: disable master password prompt (use with caution)
MASTER_PASSWORD_REQUIRED = False

# Tuning
MAX_SESSION_IDLE_TIME = 60  # minutes
UPGRADE_CHECK_ENABLED = False

###############################################################
# End of Local Configuration
###############################################################


sudo systemctl restart pgadmin4
sudo systemctl status pgadmin4  # to confirm running status




