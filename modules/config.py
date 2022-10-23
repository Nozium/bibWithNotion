from dotenv import load_dotenv
load_dotenv()

import os 
import sys 
sys.path.append(os.path.dirname(os.getcwd()))

# load config from .env files
NOTION_DB_ID = os.getenv("NOTION_DB_ID")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")


# set other statics
DEFAULT_BIB_DIR = "./bibfiles"
