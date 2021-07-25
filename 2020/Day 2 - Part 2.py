inputs = open("inputs/Day2Input.txt", "r")
valid_passwords = 0

def valid_password(input):
    value = input.split(" ")
    limits = value[0].split("-")
    lower_limit = int(limits[0])
    upper_limit = int(limits[1])
    character = value[1].strip(":")
    password = list(value[2])
    if (password[lower_limit-1] == character) ^ (password[upper_limit-1] == character):
        return True
    else:
        return False
    


input1 = "1-3 a: abcde"
input2 = "1-3 b: cdefg"
input3 = "2-9 c: ccccccccc"

assert(valid_password(input1) == True)
assert(valid_password(input2) == False)
assert(valid_password(input3) == False)

for line in inputs:
    if valid_password(line):
        valid_passwords += 1
print(valid_passwords)

