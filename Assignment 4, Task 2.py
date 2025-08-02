a=input('Enter text to write to the file: ')
print('Data successfully written to output.txt.\n')

with open('output.txt','w') as file:
    writing=file.write(a)

b=input('Enter additional text to append: ')
print('Data successfully appended.\n')

with open('output.txt','a') as file:
    appending=file.write('\n'+b)

print('Final content of output.txt:')

with open('output.txt','r') as file:
    reading=file.read()
    print(reading)