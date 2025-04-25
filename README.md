# RestaurantNameGenerator

> AI-powered restaurant branding toolkit  
> Generate catchy restaurant names and menus in seconds!

[![Streamlit](https://img.shields.io/badge/streamlit-✔️-orange)](#) [![Python](https://img.shields.io/badge/python-3.12-blue)](#) [![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🚀 Features

- **Name Generation**  
  Produce unique, on-brand restaurant names from any cuisine (Italian, Mexican, Thai, etc.).  
- **Menu Suggestions**  
  Auto-generate a curated list of menu items tailored to your restaurant name.  
- **Secure API Management**  
  Store your Google Gemini (Groq) key in a `.env` file—never checked into Git.  
- **Web UI**  
  Interactive Streamlit interface; no frontend coding required.  

---

## 📸 Screenshot

![App screenshot](docs/screenshot.png)

---

## 🛠 Tech Stack

| Component          | Technology             |
|--------------------|------------------------|
| Web UI             | Streamlit              |
| LLM Orchestration  | LangChain + ChatGroq   |
| LLM Provider       | Google Gemini (Groq)   |
| Config & Secrets   | python-dotenv (`.env`) |
| Language           | Python 3.12            |

---

## 📥 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/RestaurantNameGenerator.git
   cd RestaurantNameGenerator
