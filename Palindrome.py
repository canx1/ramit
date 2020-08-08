word = input('Please enter a word:> ')
reverse_string = ''
for char in word:
    reverse_string = char + reverse_string
    
print(reverse_string)    
    
print(word[::-1]) 