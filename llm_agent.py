# chatbot_agent/llm_agent.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_llm_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[!] 调用 OpenAI 出错: {e}")
        return None
