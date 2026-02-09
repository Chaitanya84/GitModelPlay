from openai import OpenAI
import os
##acces token from env variable
GITHUB_TOKEN = os.getenv("GITHUB_PAT")
# Initialize the OpenAI client with the GitHub token
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)

response = client.chat.completions.create(
    model="gpt-4o", # Use a supported GitHub model name
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

print(response.choices[0].message.content)