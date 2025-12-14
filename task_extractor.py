# task_assigner.py

import re

TASK_KEYWORDS = [
    "need to", "should", "have to", "must",
    "fix", "update", "design", "write", "optimize"
]

PRIORITY_KEYWORDS = {
    "critical": "High",
    "blocking": "High",
    "high priority": "High",
    "important": "High",
    "can wait": "Medium",
}

DEADLINE_KEYWORDS = [
    "tomorrow", "today", "by friday", "by monday",
    "next week", "next monday", "end of this week",
    "wednesday", "friday"
]

def extract_tasks(transcript):
    tasks = []
    sentences = transcript.lower().split(".")

    task_id = 1

    for sentence in sentences:
        if any(keyword in sentence for keyword in TASK_KEYWORDS):

            # Deadline detection
            deadline = "Not mentioned"
            for d in DEADLINE_KEYWORDS:
                if d in sentence:
                    deadline = d.title()

            # Priority detection
            priority = "Medium"
            for p in PRIORITY_KEYWORDS:
                if p in sentence:
                    priority = PRIORITY_KEYWORDS[p]

            tasks.append({
                "task_id": task_id,
                "description": sentence.strip().capitalize(),
                "deadline": deadline,
                "priority": priority
            })

            task_id += 1

    return tasks

def detect_dependencies(task_description):
    if "depends on" in task_description or "after" in task_description:
        return "Depends on previous task"
    return None
