import os

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("API_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("API_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")
