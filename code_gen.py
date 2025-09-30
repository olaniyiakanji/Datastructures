import random
import string

def generate_code(length=8):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage
print(generate_code())      # e.g., 'A9dX3pQz'
print(generate_code(12))    # e.g., 'Z8kLm2T4yR1W'
