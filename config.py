import os
from dotenv import load_dotenv

# Load local environment variables if testing on a home computer
load_dotenv()

# THE SECRET VAULT: We pull these values safely from the hosting environment.
# Never paste your actual Token or MongoDB URI in the code!
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")

# The ID or Username of the channel users MUST subscribe to (e.g., @trinityxmods)
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "@trinityxmods")

# The private log channel for exhaustive system tracking
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "-1003476512603"))

# Database Configuration
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "trinity_cp")
