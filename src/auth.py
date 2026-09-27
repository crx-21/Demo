def validate_user(username):
    # Added null-check to prevent crash
    if username is None:
        return False
    if username:
        return True
    return False
