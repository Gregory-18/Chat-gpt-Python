import os
from dotenv import load_dotenv

load_dotenv()

#Se define una variable con la api_key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')