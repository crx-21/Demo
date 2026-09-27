def calculate_sum(a, b):
    # Added input validation for stability
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers")
    return a + b
