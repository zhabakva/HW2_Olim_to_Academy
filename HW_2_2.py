import re

try:
    f = open('input2.2.txt', 'r')
    s = f.read()
except FileNotFoundError:
    print(f"Error: The file does not exist.")
lines = s.split('\n')
list_to_delete = input("Enter the list of symbols to delete without separators:")
symbols = [symbol for symbol in list_to_delete]
symbols.append(';')
try:
    with open(r"output2.2.txt", "w") as file:
        for line in lines:
            while line[-1] in symbols:
                line = line[:-1]
            file.write(line[::-1] + '\n')
except IOError as e:
    print(f"Error: Unable to write to file")
