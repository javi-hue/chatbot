from openai import OpenAI
client = OpenAI(api_key="TU_API_KEY_AQUI")

async def generate_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content
