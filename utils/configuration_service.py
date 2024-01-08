import os
from dotenv import load_dotenv

load_dotenv()

configuration_service = {"mongodb_uri": os.getenv("MONGODB_URI")}
