def solve(program, input):
    if program == [] : return input
    for b in range(8):
        a = input << 3 | b
        b = a % 8
        b = b ^ 1
        c = a >> b
        b = b ^ c
        b = b ^ 4
        if b % 8 == program[-1]:
            x = solve(program[:-1], a)
            if x is None: 
                continue
            return x
    
with open("data.txt") as f:
    for i in range(4):
        f.readline()
    
    program = [int(x) for x in f.readline().split()[1].split(",")]
    
    # print(program)
    print(solve(program,0))