import dotenv
import os

dotenv.load_dotenv()
steam_token = os.getenv("STEAM_TOKEN")
if not steam_token:
    raise ValueError("STEAM_TOKEN is not defined in environment variables or .env file")