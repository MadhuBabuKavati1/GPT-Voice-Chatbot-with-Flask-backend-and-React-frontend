# smart_chatbot.py

import openai
from openai import OpenAI

# Replace with your actual API key
client = OpenAI(api_key="***REMOVED***proj-rWY33N6PDnbrIcU-MmOPQqtYKmmnaejFNohx7-TfvJiPcOGzz1rrkeno-NhE25vQomMNHnp_wCT3BlbkFJ5_Krh2MXBkKQU7_Cp7Rhlf_RpYbbc2L6Ks_bWYClXxTlXbqwt7mF3OHl_kjtUlUsSpb9kHCQ8A")

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"

def main():
    print("🤖 Smart ChatBot (GPT) — type 'exit' to quit\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋")
            break

        response = ask_gpt(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
