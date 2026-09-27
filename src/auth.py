import re
def validate_user(username):
    # New regex-based email validation
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", username))
