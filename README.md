# Jarvis – AI Voice Assistant 🎙️

Jarvis is a Python-based voice assistant that listens for a wake word, recognizes voice commands, and performs different tasks using Python libraries, external APIs, and Google Gemini AI.

## 🚀 Features

- **Wake Word Detection:** Activates when the user says "Jarvis".
- **Voice Recognition:** Recognizes spoken commands using Speech Recognition.
- **Website Navigation:** Opens websites such as Google and YouTube through voice commands.
- **Music Playback:** Plays songs using predefined music links.
- **News Updates:** Fetches and speaks the latest news headlines using NewsAPI.
- **AI-Powered Conversations:** Uses Google Gemini AI to answer general questions.
- **Text-to-Speech:** Responds verbally using pyttsx3.
- **Exit Command:** Shuts down the assistant when requested.

## 🛠️ Technologies Used

- Python
- Google Gemini API
- SpeechRecognition
- PyAudio
- pyttsx3
- Requests
- NewsAPI
- Webbrowser

## 📂 Project Structure

```text
Jarvis-Voice-Assistant/
│
├── main.py
├── musiclibrary.py
├── api.py
├── requirements.txt
└── README.md
```

**Note:** `api.py` contains API credentials and should remain private. Do not upload it to GitHub.

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/jarvis-voice-assistant.git
```

2. Navigate to the project directory:

```bash
cd jarvis-voice-assistant
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Configure your API credentials locally in `api.py`:

```python
news_api = "YOUR_NEWS_API_KEY"
gemini_api = "YOUR_GEMINI_API_KEY"
```

6. Run the assistant:

```bash
python main.py
```

## 🎯 How to Use

1. Run the Python application.
2. Say **"Jarvis"** to activate the assistant.
3. Speak a command, such as:
   - "Open Google"
   - "Open YouTube"
   - "Play [song name]"
   - "News"
   - "Who is Hrithik Roshan?"
   - "Exit"

## 🔐 Important

- A working microphone and internet connection are required.
- Google Gemini and NewsAPI credentials are required.
- Keep API keys private. Never commit `api.py` or other files containing secrets.
- Music playback depends on the song links configured in `musiclibrary.py`.

## 👨‍💻 Author

**Priyanshu Kumar Singh**

BSc Computer Science & Data Analytics  
IIT Patna
