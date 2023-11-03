from os import getenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
DB_URI = getenv("DB_URI")

if not DB_URI:
    print('Pls add a DB_URI to your env file')
    exit()
