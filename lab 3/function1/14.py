from task_functions import histogram, guess_the_number, sphere_volume, unique_elements, is_palindrome

print("Histogram:")
histogram([4, 9, 7])

print("\nLet's play 'Guess the Number' game!")
guess_the_number()

radius = 3
print(f"\nVolume of a sphere with radius {radius}: {sphere_volume(radius):.2f}")

nums = [1, 2, 2, 3, 4, 4, 5]
print(f"\nUnique elements from {nums}: {unique_elements(nums)}")

word = "madam"
print(f"\nIs the word '{word}' a palindrome? {is_palindrome(word)}")