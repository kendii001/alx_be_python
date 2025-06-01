# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process task based on priority using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority level"

# Check if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["high", "medium", "low"]:
        message += ". Consider completing it when you have time."

# Display the final reminder
print("\n" + message)
