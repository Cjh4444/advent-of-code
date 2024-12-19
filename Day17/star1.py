registers = {"A": [0], "B": [0], "C": [0]}
combo_operand_map = [(0,),(1,),(2,),(3,),registers["A"],registers["B"],registers["C"]]
program = []
pointer = 0
output = []

def adv():
    operand = int(program[pointer + 1])
    registers["A"][0] = int(registers["A"][0] / (2 ** combo_operand_map[operand][0]))

def bxl():
    operand = int(program[pointer + 1])
    registers["B"][0] = registers["B"][0] ^ operand

def bst():
    operand = int(program[pointer + 1])
    registers["B"][0] = combo_operand_map[operand][0] % 8

def jnz() -> int:
    if registers["A"][0] == 0:
        return pointer + 2
    
    operand = int(program[pointer + 1])
    return operand

def bxc():
    operand = int(program[pointer + 1])
    registers["B"][0] = registers["B"][0] ^ registers["C"][0]

def out():
    operand = int(program[pointer + 1])
    output.append(str(combo_operand_map[operand][0] % 8))

def bdv():
    operand = int(program[pointer + 1])
    registers["B"][0] = int(registers["A"][0] / (2 ** combo_operand_map[operand][0]))

def cdv():
    operand = int(program[pointer + 1])
    registers["C"][0] = int(registers["A"][0] / (2 ** combo_operand_map[operand][0]))
    

    
with open("data.txt") as f:
    registers["A"][0] = int(f.readline().split()[2])
    registers["B"][0] = int(f.readline().split()[2])
    registers["C"][0] = int(f.readline().split()[2])
    
    f.readline()
    
    program = f.readline().split()[1].split(",")
    
    print(registers)
    while pointer < len(program):
        opcode = program[pointer]
        if opcode == "0":
            adv()
        elif opcode == "1":
            bxl()
        elif opcode == "2":
            bst()
        elif opcode == "3":
            pointer = jnz()
            continue
        elif opcode == "4":
            bxc()
        elif opcode == "5":
            out()
        elif opcode == "6":
            bdv()
        elif opcode == "7":
            cdv()
        pointer += 2
    print(",".join(output))
    print(registers)