def snake_to_camel(snake_str):
    words = snake_str.split("_")
    camel_case = words[0].lower() + "".join(word.capitalize() for word in words[1:])
    return camel_case

snake_str = input("Enter snake_case: ")

camel_str = snake_to_camel(snake_str)

print("CamelCase:", camel_str)
