try:
    f1 = open('input2.3.1.txt', 'r')
    s1 = f1.read()
except FileNotFoundError:
    print(f"Error: The file does not exist.")
lines1 = s1.split('\n')
try:
    f2 = open('input2.3.2.txt', 'r')
    s2 = f2.read()
except FileNotFoundError:
    print(f"Error: The file does not exist.")
lines2 = s2.split('\n')
lines = lines1 + lines2
lines.sort()
try:
    with open(r"output2.3.txt", "w") as file:
        for line in lines:
            file.write(line + '\n')
except IOError as e:
    print(f"Error: Unable to write to file")
