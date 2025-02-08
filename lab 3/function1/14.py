import random
import math

def histogram(lst):
    for num in lst:
        print('*' * num)

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        try:
            guess = int(input())
            guesses_taken += 1
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
                break
        except ValueError:
            print("Please enter a valid number!")

def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]