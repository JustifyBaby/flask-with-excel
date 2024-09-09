import subprocess


def run_command():
    commands = [
        "Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force",
        "./.main/Scripts/activate",
        '$env:FLASK_APP="pages"',
        '$env:FLASK_ENV="development"',
    ]

    for current_running, command in enumerate(commands):
        subprocess.call(command)
        print(f"No.{current_running + 1} ran successfully!!")
