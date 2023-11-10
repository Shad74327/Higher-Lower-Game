from art import logo, vs
from game_data import data
import random
print(logo)

compare_A = random.choice(data)
score = 0

while True:
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}.")
    print(vs)
    compare_B = random.choice(data)
    print(f"Compare B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer == "A":
        if compare_A['follower_count'] > compare_B['follower_count']:
            score+=1
            print(f"You're right! Current score: {score}")
            compare_A = compare_B
            
        elif compare_A['follower_count'] < compare_B['follower_count']:
            print(f"Sorry that's wrong! Final score: {score}")
            break

    elif answer == "B":
        if compare_B['follower_count'] > compare_A['follower_count']:
            score+=1
            print(f"You're right! Current score: {score}")
            compare_A = compare_B

        elif compare_B['follower_count'] < compare_A['follower_count']:
            print(f"Sorry that's wrong! Final score: {score}")
            break

    else:
        print("Invalid answer!")
        break