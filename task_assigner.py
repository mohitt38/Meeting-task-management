# assigner.py

from team import TEAM_MEMBERS

def assign_tasks(tasks):
    for task in tasks:
        description = task["description"].lower()
        assigned_to = "Unassigned"
        reason = "No matching rule"

        # 1️⃣ Explicit name mention
        for member in TEAM_MEMBERS:
            if member["name"].lower() in description:
                assigned_to = member["name"]
                reason = "Name explicitly mentioned"
                break

        # 2️⃣ Skill-based matching
        if assigned_to == "Unassigned":
            for member in TEAM_MEMBERS:
                for skill in member["skills"]:
                    if skill in description:
                        assigned_to = member["name"]
                        reason = f"Matched skill: {skill}"
                        break
                if assigned_to != "Unassigned":
                    break

        task["assigned_to"] = assigned_to
        task["reason"] = reason

    return tasks
