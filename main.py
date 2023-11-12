from art import logo, vs
from game_data import data
import random
print(logo)

compare_A = random.choice(data)
score = 0

def answer_check(compare_A, compare_B):
    """Checking the user input and generating an output accordingly"""

    if compare_A['follower_count'] > compare_B['follower_count']:
        return answer=="a"
    else:
        return answer=="b"

while True:
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}.")
    print(vs)
    compare_B = random.choice(data)

    while compare_A == compare_B:
        compare_B = random.choice(data)
    
    print(f"Compare B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    while answer != "a" and answer != "b":
        """Checking for an invalid answer."""
        
        answer = input("Invalid answer! Type 'A' or 'B': ").lower()

    is_correct = answer_check(compare_A, compare_B)

    if is_correct == True:
        score+=1
        print(f"You're right! Current score: {score}")
        compare_A = compare_B
    else:
        print(f"Sorry that's wrong! Final score: {score}")
        break 