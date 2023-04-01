import os
from dotenv import load_dotenv
load_dotenv()

def generate_text(prompt):
    import openai
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    print("API key: ", openai.api_key)
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=1,
                                        max_tokens=280)
    return response.choices[0].text


print(generate_text("Tell me a bad joke"))
