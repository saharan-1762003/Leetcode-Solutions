import os

number = input("Problem Number : ").strip()
name = input("Problem Name   : ").strip()
difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
topic = input("Topic          : ").strip()
language = input("Language (cpp/python/java): ").strip().lower()

folder_name = f"{int(number):04d}-{name.replace(' ', '-')}"

topic_path = os.path.join(topic)

os.makedirs(topic_path, exist_ok=True)

problem_path = os.path.join(topic_path, folder_name)

os.makedirs(problem_path, exist_ok=True)

extension = {
    "cpp":"cpp",
    "python":"py",
    "java":"java"
}.get(language,"txt")

solution_file = os.path.join(problem_path,f"solution.{extension}")

with open(solution_file,"w") as f:
    pass

readme = f"""# {number}. {name}

Difficulty : {difficulty}

## Approach



## Complexity

Time :

Space :
"""

with open(os.path.join(problem_path,"README.md"),"w") as f:
    f.write(readme)

print("\n✅ Problem folder created successfully!")
print(problem_path)