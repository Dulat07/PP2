def reverse_words(sentence):
   
    words = sentence.split() 
    reversed_words = words[::-1]  
    return ' '.join(reversed_words)  

user_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(user_sentence)
print("Reversed sentence:", reversed_sentence)