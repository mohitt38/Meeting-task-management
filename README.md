### 🎙️ Meeting Task Assignment System

## Overview

The Meeting Task Assignment System automatically processes meeting audio recordings and extracts actionable tasks discussed during the meeting. The system assigns tasks to appropriate team members and identifies deadlines, priorities, and dependencies using rule-based logic.

Problem Statement

In team meetings, multiple tasks are discussed verbally and need to be manually noted and assigned. This process is time-consuming and error-prone.
The goal of this project is to automate task identification and assignment from meeting audio recordings.

## Features

Converts meeting audio to text using Speech-to-Text

Extracts tasks using keyword-based rules (no ML models)

Assigns tasks to team members based on names, roles, and skills

Detects deadlines and priority levels

Identifies task dependencies

Displays results in a table and exports output as JSON

## Tech Stack

Python

Streamlit

Whisper (Speech-to-Text)

FFmpeg

Pandas

How It Works

Upload a meeting audio file (.mp3, .wav, .m4a)

Audio is transcribed into text

Tasks are identified using rule-based NLP logic

Tasks are assigned to appropriate team members

Deadlines, priorities, and dependencies are extracted

Final output is displayed and saved as JSON

## Installation
pip install -r requirements.txt

Run the Application
streamlit run app.py

Output

Interactive task table displayed on the UI

Downloadable JSON file: output_tasks.json

Constraints Followed

No external APIs or ML models used for task classification or assignment

Only Speech-to-Text uses an external model

All task identification and assignment logic is rule-based

## Screenshots

Upload Meeting Audio
![Upload Meeting Audio](screenshots\process.png)

Extracted and Assigned Tasks
![Task Assignment Table](screenshots\table.png)





## Project Structure
meeting-task-assignment/
│
├── app.py
├── stt.py
├── task_extractor.py
├── assigner.py
├── team_members.py
├── requirements.txt
├── output_tasks.json
├── sample_audio/
│   └── meeting.mp3
└── README.md