user_input = input('Please enter a number between 1 and 12:> ')

while (not user_input.isdigit()) or (int(user_input) < 1 or int(user_input) >12):
    print('Must be an integer between 1 and 12')
    user_input = input('Please make correct selection:> ' )
user_input = int(user_input)
print('===============================')
print()
print(f'This is the {user_input} times table')
print()
for i in range(1,11):
    print(f'{i} x {user_input} = {i*user_input}')
