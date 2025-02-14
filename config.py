import os
from dotenv import load_dotenv

load_dotenv()

LOGIN = str(os.getenv('LOGIN'))
PASSWORD = str(os.getenv('PASSWORD'))
BASE_URL = str(os.getenv('BASE_URL'))
