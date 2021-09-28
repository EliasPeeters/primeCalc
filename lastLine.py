last_line = 2

with open("data.txt", "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass

print(last_line)
