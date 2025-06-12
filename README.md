# 📝 Voice-to-Meeting Notes + Task Tracker

**Your AI-powered meeting assistant** that listens to voice recordings and extracts the essence: a clean summary, key points, and action items assigned to each participant.

Built with 🧠 Google Gemini AI and ElevenLabs’ speech-to-text engine, this tool turns your team huddles, project updates, and client calls into actionable insights with just a single upload.

## 🚀 Features

- 🎙️ Speech-to-Text: Automatically transcribes English audio using ElevenLabs.
- 🧠 AI Summarization: Google Gemini summarizes your meetings into digestible content.
- ✅ Action Item Extraction: Detects responsibilities and tasks per participant.
- 👥 Participant Mapping: Smartly tags tasks to the right people based on names provided.
- 🌐 Multiformat Audio Support: Accepts `.mp3` and `.wav` files.
- ⚡ Streamlit UI: Lightweight, interactive web app with a clean user experience.

## 🛠️ Tech Stack

| Tool / Library          | Role                                      |
|-------------------------|-------------------------------------------|
| Streamlit               | Frontend Web App Interface                |
| ElevenLabs API          | Speech-to-Text Transcription              |
| Google Generative AI    | Summarization & Task Extraction           |
| langdetect              | Language Detection (English-only filter)  |
| requests                | API Integration                           |
| Python                  | Core Programming Language                 |

## 🧩 Installation

1. **Clone the Repo**
   ```bash
   git clone https://github.com/saadnaveeddev/voice-meeting-assistant).git
   cd voice-task-tracker
   ```

2. **(Optional) Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add API Keys**
   Edit the script or use environment variables:
   ```python
   ELEVEN_API_KEY = "your_elevenlabs_api_key"
   GENAI_API_KEY = "your_google_genai_api_key"
   ```

## 🧪 Usage

1. Launch the app:
   ```bash
   streamlit run app.py
   ```

2. Upload your audio file (`.mp3` or `.wav`).

3. Enter the names of the participants (comma-separated).

4. Get instant:
   - 📋 Transcription
   - ✍️ Summary
   - ✅ Key decisions
   - 📌 Tasks tagged to each participant

## 🧠 Memory System

Currently **stateless**, but easily extensible:
- Add `st.session_state` for temporary context.
- Use Firebase/Supabase/PostgreSQL for persistent task logs.
- Integrate with Google Meet, Zoom, or Slack for real-time sync.

## 📦 Example Output

```
### Summary:
The team discussed upcoming feature launches, delegated QA tasks, and confirmed the new deployment timeline.

### Key Points:
- Beta release set for next Friday.
- QA to begin this weekend.
- Areeba to coordinate with frontend team.

### Tasks by Participant:
- **Areeba**: Coordinate with frontend and report blockers.
- **Saad**: Oversee deployment pipeline and ensure logging.
- **Bilal**: Conduct QA testing and document issues.
```

## 👨‍💻 Author

**Saad Naveed**  
AI Research Engineer | Data Scientist | GenAI Innovator  
🔗 [LinkedIn](https://www.linkedin.com/in/saadnaveed753/)  
🐙 [GitHub](https://github.com/saadnaveeddev)

## 💡 Future Enhancements

- 🔄 Real-time meeting capture (Twilio/Zoom integration)
- 📧 Email summaries to participants
- 🗂️ Export notes as PDF or Markdown
- 📊 Project dashboard for task tracking
- 🌍 Support for more languages

## 📜 License

MIT License  
*Build, share, iterate — just don’t forget to credit the nerd who built it 😎*

> “Let the AI handle the minutes, so you can focus on the meeting.”
