import re

try:
    f = open('input2.1.txt', 'r')
    s = f.read()
except FileNotFoundError:
    print(f"Error: The file does not exist.")
dict = {"name": -1}

lines = s.split('\n')
count = 0
age_sum = 0
for line in lines:
    count += 1
    name = line.split(',')[0]
    age = line.split(',')[1]
    name_new = re.sub(r'[^\w\s]', '', name)
    age_new = int(re.sub(r'[^\w\s]', '', age))
    age_sum += age_new
    dict.update({name_new: age_new})
if count != 0:
    middle_age = age_sum/count
    #print(middle_age)
try:
    with open(r"output2.1.txt", "w") as file:
        for key in dict.keys():
            if dict[key] >= middle_age:
                file.write(str(key) + '\n')
except IOError as e:
    print(f"Error: Unable to write to file")


