import os
import subprocess

# Dictionary to map scores to descriptive words
score_map = {
    1: "poor",
    2: "below average",
    3: "average",
    4: "good",
    5: "excellent"
}

# Dictionary for engagement and further learning actions
engagement_actions = {
    1: "minimally",
    2: "infrequently",
    3: "moderately",
    4: "actively",
    5: "highly actively"
}

further_learning_actions = {
    1: "basic coding concepts",
    2: "fundamental programming principles",
    3: "intermediate coding challenges",
    4: "advanced project building",
    5: "specialisation in a chosen field"
}

# Create a directory for the reports
os.makedirs("student_feedback", exist_ok=True)

# Prompt the user to input names
names = input("Enter the names of students, separated by commas: ").split(",")
names = [name.strip() for name in names]  # Remove extra spaces

# Feedback template
template = """
General Comments:
{name} has good knowledge of programming principles and did {understanding} in this module. 
{name} contributed {contribution} to group discussions and worked well in groups.

Learner Punctuality and Engagement:
{name} was {punctuality} throughout the module and engaged {engagement} with camera on.

Recommendations on Further Learning:
Continue to practice and explore {further_learning}.
"""

# Generate feedback for each student
for name in names:
    print(f"\nGenerating feedback for {name}...\n")
    
    # Prompt for scores
    understanding = int(input(f"Understanding level for {name} (1-5): "))
    contribution = int(input(f"Contribution level for {name} (1-5): "))
    punctuality = int(input(f"Punctuality level for {name} (1-5): "))
    engagement = int(input(f"Engagement level for {name} (1-5): "))
    further_learning = int(input(f"Further learning level for {name} (1-5): "))

    # Apply the template
    feedback = template.format(
        name=name,
        understanding=score_map[understanding],
        contribution=score_map[contribution],
        punctuality=score_map[punctuality],
        engagement=engagement_actions[engagement],
        further_learning=further_learning_actions[further_learning]
    )

    # Save the feedback to a text file
    file_path = f"student_feedback/{name}.txt"
    with open(file_path, "w") as file:
        file.write(feedback)

    print(f"Feedback for {name} saved at {file_path}.")
    
    subprocess.call(["notepad", file_path])  # For Windows
# On Mac/Linux, use: subprocess.call(["open", file_path])

print("\nAll feedback reports have been generated.")
