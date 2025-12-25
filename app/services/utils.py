import re

def extract_package(input_value: str):
    # Case 1: Play Store URL
    match = re.search(r"id=([a-zA-Z0-9._]+)", input_value)
    if match:
        return match.group(1)

    # Case 2: User pasted package name directly
    if "." in input_value:
        return input_value.strip()

    # Case 3: App name (handled later)
    return None
