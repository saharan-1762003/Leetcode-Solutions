import os
import subprocess

print("=" * 50)
print("🚀 LeetCode Repository Manager")
print("=" * 50)

# Input
number = int(input("Problem Number : "))
name = input("Problem Name : ").strip().title()
topic = input("Topic : ").strip().title()
language = input("Language (cpp/python/java): ").strip().lower()

# Folder name
folder_name = f"{number:04d}-{'-'.join(name.split())}"

# Create folder structure
problem_path = os.path.join(topic, folder_name)
os.makedirs(problem_path, exist_ok=True)

# File extension
extensions = {
    "cpp": "cpp",
    "python": "py",
    "java": "java"
}

extension = extensions.get(language, "txt")
solution_file = os.path.join(problem_path, f"solution.{extension}")

print("\nPaste your solution below.")
print("When finished:")
print("👉 Windows: Press Ctrl+Z and then Enter")
print("👉 Linux/macOS: Press Ctrl+D")
print("-" * 50)

# Read solution
lines = []

try:
    while True:
        lines.append(input())
except EOFError:
    pass

code = "\n".join(lines)

# Save solution
with open(solution_file, "w", encoding="utf-8") as f:
    f.write(code)

print(f"\n✅ Created: {solution_file}")

# Git operations
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"Solve {folder_name}"],
        check=True
    )
    subprocess.run(["git", "push"], check=True)

    print("\n🚀 Successfully pushed to GitHub!")

except subprocess.CalledProcessError:
    print("\n⚠ Git operation failed.")
    print("Please check your git configuration or internet connection.")