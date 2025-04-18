# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key="***REMOVED***proj-rWY33N6PDnbrIcU-MmOPQqtYKmmnaejFNohx7-TfvJiPcOGzz1rrkeno-NhE25vQomMNHnp_wCT3BlbkFJ5_Krh2MXBkKQU7_Cp7Rhlf_RpYbbc2L6Ks_bWYClXxTlXbqwt7mF3OHl_kjtUlUsSpb9kHCQ8A")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("message")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        message = response.choices[0].message.content
        return jsonify({"reply": message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
