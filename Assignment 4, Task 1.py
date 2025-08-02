try:
    print('Reading file content:')
    with open('sample.txt', 'r+') as file:
        file.write('Line 1: This is a sample text file.')
        file.write('\nLine 2: Its contains multiple lines.')
    with open('sample.txt', 'r+') as file:
        reading = file.read()
        print(reading)

except:
    print("Error: The file 'sample.txt' was not found.")
