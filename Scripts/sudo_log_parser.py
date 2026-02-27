import re
from collections import defaultdict

LOG_FILE = "../logs/sample_auth.log"

sudo_pattern = re.compile(r"sudo: .*authentication failure")
user_pattern = re.compile(r"user=(\w+)")

user_attempts = defaultdict(int)

try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            if sudo_pattern.search(line):
                user_match = user_pattern.search(line)
                if user_match:
                    user = user_match.group(1)
                    user_attempts[user] += 1

    print("\n=== Sudo Authentication Failure Summary ===\n")

    for user, count in user_attempts.items():
        print(f"User: {user}")
        print(f"Failed Sudo Attempts: {count}")

        if count >= 3:
            print("⚠ Potential Privilege Escalation Detected\n")
        else:
            print()

except FileNotFoundError:
    print("Log file not found. Please check file path.")