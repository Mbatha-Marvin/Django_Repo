import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ["OPEN_AI_API_KEY"]
openai.api_key=openai_api_key

model_engine = "text-davinci-003"

def get_response(prompt: str) -> str:

    response = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens=1024,
        n = 1,
        stop = None,
        temperature = 0,
    )

    # print(response.choices[0].text)

    return response.choices[0].text