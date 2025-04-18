// src/App.js

import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  // 🎤 Start voice input (Speech-to-Text)
  const startListening = () => {
    const recognition = new window.webkitSpeechRecognition(); // Use SpeechRecognition in Firefox
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.onresult = (event) => {
      const voiceText = event.results[0][0].transcript;
      setMessage(voiceText);
      sendMessage(voiceText); // Auto-send after speaking
    };
    recognition.start();
  };

  // 🔊 Speak bot's reply (Text-to-Speech)
  const speak = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    window.speechSynthesis.speak(utterance);
  };

  const sendMessage = async (customMessage) => {
    const input = customMessage || message;

    if (!input.trim()) return;

    const newChat = [...chat, { type: "user", text: input }];
    setChat(newChat);
    setMessage("");

    try {
      const res = await axios.post("http://127.0.0.1:5000/api/chat", {
        message: input,
      });
      const reply = res.data.reply;
      setChat([...newChat, { type: "bot", text: reply }]);
      speak(reply); // ✅ Bot speaks response
    } catch (err) {
      setChat([
        ...newChat,
        { type: "bot", text: "❌ Error: " + err.message },
      ]);
    }
  };

  return (
    <div className="App">
      <h2>💬 GPT Web Chatbot</h2>

      <div className="chat-box">
        {chat.map((msg, idx) => (
          <div key={idx} className={msg.type}>
            <b>{msg.type === "user" ? "You:" : "Bot:"}</b> {msg.text}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type or speak your message..."
        />
        <button onClick={() => sendMessage()}>Send</button>
        <button onClick={startListening}>🎤</button>
      </div>
    </div>
  );
}

export default App;
