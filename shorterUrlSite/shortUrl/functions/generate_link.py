import string
import random


def generate():
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(5))
    print(result)
    
    return result
