testinputs = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

testinputs = testinputs.split("\n\n")

def check_passport(input):
    field_list = []
    value = input.split()
    for thing in value:
        thing = thing[0:3]
        field_list.append(thing)
    required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    for field in required_fields:
        if field not in field_list:
            return False
    return True

def count_valid_passports(inputs):
    valid_passports = 0
    for item in inputs:
        if check_passport(item):
            valid_passports += 1
    return valid_passports


assert(count_valid_passports(testinputs) == 2)

with open("inputs/Day4Input.txt", "r") as f:
    inputfile = f.read().split("\n\n")
    print(count_valid_passports(inputfile))



