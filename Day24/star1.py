input_to_output_dict: dict[str, list[str]] = {}

with open("data.txt") as f:
    _ = f.read().split("\n\n")
    
    start_vals = _[0].split("\n")
    vals_to_check = _[1].split("\n")

    register_to_binary = {}

    for _ in start_vals:
        string, binary_val = _.split(":")
        register_to_binary[string] = int(binary_val)
        
    for x in vals_to_check:
        split_str = x.split("->")
        input_to_output_dict.setdefault(split_str[0].strip(), []).append(split_str[1].strip())
    
    inputs = set(input_to_output_dict.keys())
    
    while inputs:
        input_to_check = inputs.pop()
        outputs = input_to_output_dict[input_to_check]
        
        left, op, right = input_to_check.split()
        
        val = 0
        
        if left in register_to_binary and right in register_to_binary:
            if op == "AND":
                val = register_to_binary[left] and register_to_binary[right]
            elif op == "OR":
                val = register_to_binary[left] or register_to_binary[right]
            elif op == "XOR":
                val = register_to_binary[left] ^ register_to_binary[right]
            
            for output in outputs:
                register_to_binary[output] = val
        else:
            inputs.add(input_to_check)
        
    z_dict = {}
    
    for register, binary in register_to_binary.items():
        if register.startswith("z"):
            z_dict[register] = binary
        
    num = 0
    for mult, x in enumerate(sorted(list(z_dict.keys())[::-1])):
        num += z_dict[x] * 10 ** mult
    
    print(int(str(num), 2))