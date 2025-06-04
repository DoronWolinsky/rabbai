from openai import OpenAI
import os

client = OpenAI()  # Will automatically use the OPENAI_API_KEY environment variable

def get_rabbi_answer(question, rabbi_type="Ashkenazi"):
    prompt = f"""
    You are a {rabbi_type} rabbi. A follower asks: '{question}'.
    Please answer according to {rabbi_type} Jewish traditions, quoting relevant sources if possible. Be kind and respectful. 

    **Important**: This is not a binding halachic ruling, but rather guidance based on Jewish texts and traditions. 
    If unsure, please encourage the follower to consult a rabbi for a definitive ruling.
    """

    # Use chat completion (chat-style interaction)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful and knowledgeable rabbi."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# Input
question = input("Ask a question: ")
rabbi_type = input("Rabbi type (e.g., Ashkenazi, Sephardic): ")
answer = get_rabbi_answer(question, rabbi_type)

print("\nRabbi's Answer:\n")
print(answer)

