
from openai import OpenAI
from dotenv import load_dotenv
import os
from models.meditation import MeditationResponse


load_dotenv() 



def main():
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

    completion = client.beta.chat.completions.parse(
        model=os.environ.get("OPENAI_MODEL"),
        messages=[
            {"role": "system", "content": "You are a helpful psychologist."},
            {"role": "user", "content": "Can you make a 45 second mindfulness meditation?"},
        ],
        response_format=MeditationResponse,
    )

    message = completion.choices[0].message
    if message.parsed:
        print(message.parsed.steps)
        print('\n')
        print(message.parsed.final_answer)
    else:
        print(message.refusal)

if __name__ == "__main__":
    main()