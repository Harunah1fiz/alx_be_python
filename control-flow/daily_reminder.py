task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low):" )
time_bond = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bond == "yes":
            print(f"Reminder: '{task_description}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Note: '{task_description}' is a {priority} task. Consider completing it when you have free time.")
    case "medium":
        if time_bond == "yes":
            print(f"Reminder: '{task_description}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Note: '{task_description}' is a {priority} task. Consider completing it when you have free time.")
    case "low":
        if time_bond == "yes":
            print(f"Reminder: '{task_description}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Note: '{task_description}' is a {priority} task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")