from openai import OpenAI
import os
from dotenv import load_dotenv


# Load env variables .env
load_dotenv()


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv('OPENAI_API_KEY'),
)
# openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_blog(paragraph_topic):
    completion = client.chat.completions.create(
        extra_headers={},
        extra_body={},
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": 'Write a paragraph about the following topic. '
                           + paragraph_topic,
            }
        ]
    )

    retrieve_blog = completion.choices[0].message.content

    return retrieve_blog


print(generate_blog('Ciekawostki o Pieńsku - Małym mieście na Dolnym Śląsku.'))
