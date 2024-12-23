import cohere
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("cohere_key")
co = cohere.Client(key)


def get_response(user_input):
    response =  co.chat(
    model="command-r-plus",
    message=user_input
    )
    return response.text