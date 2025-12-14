import streamlit as st
from stt import transcribe_audio
from task_extractor import extract_tasks, detect_dependencies
from task_assigner import assign_tasks
import pandas as pd
import json

st.set_page_config(page_title="Meeting Task Assignment", layout="wide")

st.title("🎙️ Meeting Task Assignment System")

audio_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["wav", "mp3", "m4a"]
)

if audio_file:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())

    if st.button("Process Meeting"):
        with st.spinner("Processing..."):
            transcript = transcribe_audio("temp_audio.wav")
            tasks = extract_tasks(transcript)
            tasks = assign_tasks(tasks)

            for task in tasks:
                task["dependency"] = detect_dependencies(task["description"].lower())

        st.subheader("📝 Transcript")
        st.text_area("Transcript", transcript, height=200)

        st.subheader("📌 Final Task Assignment")
        df = pd.DataFrame(tasks)
        st.dataframe(df, hide_index=True)

        # ✅ JSON EXPORT (INSIDE BUTTON BLOCK)
        with open("output_tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)

        st.success("Final task assignment saved as output_tasks.json")

        st.download_button(
            label="Download Output JSON",
            data=json.dumps(tasks, indent=4),
            file_name="output_tasks.json",
            mime="application/json"
        )
