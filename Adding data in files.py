# create a new file that contains 5 capitals in the same line.
#request user to add capital city and then print

file1 = open('capitals.txt','w')
file1.write('London, ')
file1.write('Paris, ')
file1.write('Madrid, ')
file1.write('Lisbon, ')
file1.write('Rome,')
file1 = open('capitals.txt','r')
print(file1.read())
file1.close()

user_input = input('Plese enter a capital city:> ')

with open('capitals.txt','a') as file:
    file.write('\n'+user_input)
    
with open('capitals.txt','r') as file1:
    print(file1.read())