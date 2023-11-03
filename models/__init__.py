from os import getenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")

DB_URI = DB_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@localhost:3306/{DB_NAME}"

env_values = {"DB_NAME": DB_NAME, "DB_USER": DB_USER, "DB_PASS": DB_PASS}
missing_values = {key for key, value in env_values.items() if not value}
if missing_values:
    print('Error: Missing env values:', missing_values)
    exit()
