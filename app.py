import streamlit as st
import requests
import google.generativeai as genai
import os
from langdetect import detect

# --- Configuration ---
ELEVEN_API_KEY = "elevenlabs-api"
GENAI_API_KEY = "genai-api"
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# --- Transcription Function ---
def speech_to_text(audio_path):
    try:
        url = "https://api.elevenlabs.io/v1/speech-to-text"
        headers = {"xi-api-key": ELEVEN_API_KEY}
        files = {"file": open(audio_path, "rb")}
        data = {
            "model_id": "scribe_v1",
            "tag_audio_events": True
        }

        response = requests.post(url, headers=headers, files=files, data=data)
        files["file"].close()

        if response.status_code == 200:
            response_data = response.json()
            transcription = response_data.get("text", "").strip()

            if not transcription:
                st.error("No transcription found in the audio.")
                return None

            detected_lang = detect(transcription)
            if detected_lang != "en":
                st.error(f"Audio is not in English (detected: {detected_lang})")
                return None

            return transcription
        else:
            st.error(f"API Error: {response.status_code}, Details: {response.json()}")
            return None

    except Exception as e:
        st.error(f"Transcription error: {e}")
        return None

# --- Summarization & Task Extraction ---
def generate_meeting_notes(transcript, participants):
    participant_list = ", ".join(participants)
    prompt = f"""
You're a corporate meeting assistant AI. You will be provided with a transcription of a meeting and a list of participant names.
First, generate a concise summary of the meeting. 
Then, extract 3-5 key bullet points that capture major decisions, action items, or updates.
Finally, identify and list any tasks or responsibilities assigned to each participant (only those in the provided list).

Transcription:
\"\"\"{transcript}\"\"\"

Participants: {participant_list}

Respond in the following format:
### Summary:
<short paragraph summary>

### Key Points:
- Point 1
- Point 2
- ...

### Tasks by Participant:
- **Name 1**: task(s) assigned
- **Name 2**: task(s) assigned
- ...
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# --- Streamlit UI ---
st.set_page_config(page_title="📞 Voice to Notes + Tasks", page_icon="📝")
st.title("📝 Task Tracker")
st.caption("Upload your meeting audio, get a summary, key points, and who's doing what!")

uploaded_audio = st.file_uploader("Upload MP3/WAV file", type=["mp3", "wav"])
participants_input = st.text_input("Enter names of people in the meeting (comma-separated)", placeholder="e.g. Saad, Areeba, Bilal")

if uploaded_audio and participants_input:
    with st.spinner("Processing audio..."):
        # Save temp file
        audio_path = os.path.join("temp_audio", uploaded_audio.name)
        os.makedirs("temp_audio", exist_ok=True)
        with open(audio_path, "wb") as f:
            f.write(uploaded_audio.read())

        transcript = speech_to_text(audio_path)

    if transcript:
        st.subheader("🗣️ Transcription")
        st.write(transcript)

        participants = [name.strip() for name in participants_input.split(",") if name.strip()]

        with st.spinner("Analyzing meeting notes and tasks..."):
            notes = generate_meeting_notes(transcript, participants)

        st.subheader("📝 Generated Meeting Notes")
        st.markdown(notes)

        os.remove(audio_path)

else:
    st.info("Please upload an audio file and enter participant names to get started.")
