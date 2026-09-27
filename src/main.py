from utils import calculate_sum
from auth import validate_user

if __name__ == "__main__":
    if validate_user("admin"):
        print(f"The sum is: {calculate_sum(10, 20)}")
